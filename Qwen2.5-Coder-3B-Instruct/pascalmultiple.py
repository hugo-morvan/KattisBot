from math import comb

def count_multiples_of_k(N, K):
    count = 0
    for i in range(N + 1):
        for j in range(i + 1):
            if comb(i, j) % K == 0:
                count += 1
    return count

# Read input
N, K = map(int, input().split())

# Compute and print the result
print(count_multiples_of_k(N, K))
# Generator time: 4.1825 seconds