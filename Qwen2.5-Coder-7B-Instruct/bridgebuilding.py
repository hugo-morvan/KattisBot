def min_distance_sum(N, M, H, pairs):
    # Sort pairs by their height and then by their index
    pairs = sorted(pairs, key=lambda x: (H[x[0]-1], x[0]))
    
    # Initialize the total distance sum
    total_distance_sum = 0
    
    for i in range(M):
        a, b = pairs[i]
        if H[a-1] == H[b-1]:
            # Calculate the distance between the two positions
            distance = abs(b - a)
            total_distance_sum += distance
    
    return total_distance_sum

# Read input
N, M = map(int, input().split())
H = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate the result and print it
result = min_distance_sum(N, M, H, pairs)
print(result)
# Generator time: 7.8693 seconds