def find_triple_correlation(p, sequence):
    from collections import defaultdict

    def get_next_indices(sequence, digit):
        indices = []
        for i, d in enumerate(sequence):
            if d == digit:
                indices.append(i)
        return indices

    a_indices = get_next_indices(sequence, '4')
    b_indices = get_next_indices(sequence, '7')
    c_indices = get_next_indices(sequence, '9')

    triple_correlations = []

    for a_idx in a_indices:
        for n in range(1, min(p - a_idx, p // 20 + 2)):
            if a_idx + n >= p:
                continue
            b_idx = sequence.index('7', a_idx + n)
            m = b_idx - (a_idx + n)
            if m < 1:
                continue
            c_idx = sequence.index('9', b_idx + m)
            if c_idx - b_idx == m and c_idx - (a_idx + n) == n:
                triple_correlations.append((a_idx, n, b_idx, m, c_idx))

    if not triple_correlations:
        return "random sequence"

    triple_correlations.sort(key=lambda x: (x[0], x[1], x[2]))
    a_idx, n, b_idx, m, c_idx = triple_correlations[0]

    a_val = int(sequence[a_idx])
    b_val = int(sequence[b_idx])
    c_val = int(sequence[c_idx])

    return f"{a_val}({n}){b_val}({m}){c_val}"

# Input
p = int(input())
sequence = input().replace(" ", "")

# Output
print(find_triple_correlation(p, sequence))
# Generator time: 11.2782 seconds