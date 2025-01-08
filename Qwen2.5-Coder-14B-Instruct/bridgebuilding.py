def find_best_bridge(N, M, H, pairs):
    from collections import defaultdict

    # Dictionary to store positions for each height
    height_positions = defaultdict(list)
    for i in range(N):
        height_positions[H[i]].append(i)

    # Function to calculate the time without a bridge
    def time_without_bridge(a, b):
        return abs(H[a] - H[b]) + 1

    # Function to calculate the time with a bridge at positions i and j
    def time_with_bridge(a, b, i, j):
        return min(abs(a - i) + abs(b - i), abs(a - j) + abs(b - j))

    # Calculate the minimum time for each pair without any bridge
    total_time = 0
    for a, b in pairs:
        if H[a] == H[b]:
            total_time += abs(a - b)
        else:
            total_time += time_without_bridge(a, b)

    # Try building a bridge at every possible position
    best_total_time = total_time
    for height in height_positions:
        positions = height_positions[height]
        if len(positions) < 2:
            continue

        # Sort positions to ensure i < j
        positions.sort()

        # Calculate the minimum time for each pair with a bridge at positions[i] and positions[j]
        new_total_time = total_time
        for a, b in pairs:
            min_time = float('inf')
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    min_time = min(min_time, time_with_bridge(a, b, positions[i], positions[j]))
            new_total_time += min_time - time_without_bridge(a, b)

        best_total_time = min(best_total_time, new_total_time)

    print(best_total_time)

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
H = list(map(int, data[2:2 + N]))
pairs = []

for i in range(2 + N, 2 + N + 2 * M, 2):
    a = int(data[i]) - 1
    b = int(data[i + 1]) - 1
    pairs.append((a, b))

# Find the best bridge
find_best_bridge(N, M, H, pairs)
# Generator time: 67.5596 seconds