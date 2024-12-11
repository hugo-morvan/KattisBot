import sys

def decompose_rhythm(N):
    # Start with the largest possible group size
    groups = []
    while N > 0:
        if N >= 3:
            groups.append(3)
            N -= 3
        else:
            groups.append(2)
            N -= 2
    return groups

# Read input
N = int(input())

# Decompose the rhythm
decomposition = decompose_rhythm(N)

# Output the result
print(len(decomposition))
for group in decomposition:
    print(group, end=' ')
print()