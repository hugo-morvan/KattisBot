from math import comb

def expected_gems(n, d, r):
    def probability_of_distribution(d, n, k):
        return comb(d + n - 1, n - 1) * (1 / n) ** d
    
    total_probability = 0
    for gems in range(1, n * d + 1):
        prob = 0
        for i in range(r, n + 1):
            prob += comb(n, i) * probability_of_distribution(d, i, gems)
        total_probability += gems * prob
    
    return total_probability

n, d, r = map(int, input().split())
print(f"{expected_gems(n, d, r):.6f}")
# Generator time: 21.9387 seconds