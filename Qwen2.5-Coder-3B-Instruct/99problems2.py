import sys
input = sys.stdin.read
data = input().split()

# Parse input values
N = int(data[0])
Q = int(data[1])
D = [int(data[i]) for i in range(2, 2 + N)]
queries = [(int(data[i]), int(data[i + N])) for i in range(2 + N, len(data), 2)]

# Sort the difficulties
D.sort()

# Process each query
for T, D_target in queries:
    if T == 1:
        # Find the smallest index where D_i > D_target
        index = bisect.bisect_right(D, D_target)
        if index < N:
            print(D[index])
        else:
            print(-1)
    elif T == 2:
        # Find the largest index where D_i <= D_target
        index = bisect.bisect_left(D, D_target)
        if index >= 0:
            print(D[index])
        else:
            print(-1)
# Generator time: 22.3999 seconds