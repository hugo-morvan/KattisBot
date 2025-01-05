def is_stable(histogram):
    N = len(histogram)
    v = [0] * N
    for i in range(1, N - 1):
        if v[i] > 0:
            if histogram[i] + v[i] > histogram[i - 1] + v[i - 1]:
                return False
        if histogram[i] + v[i] > histogram[i + 1] + v[i + 1]:
            return False
    return True

def find_histogram(N, X):
    for perm in itertools.permutations(range(1, N + 1)):
        if sum(perm) == X:
            if is_stable(perm):
                return perm
    return [-1]

import itertools

# Read input
N, X = map(int, input().split())

# Find and print the histogram
result = find_histogram(N, X)
print(' '.join(map(str, result)))
# Generator time: 27.9209 seconds