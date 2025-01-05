def find_optimal_bridge(N, M, H, pairs):
    # Step 1: Sort the heights array
    H.sort()
    
    # Step 2: Find the longest increasing subsequence (LIS)
    lis = []
    for height in H:
        if not lis or height >= lis[-1]:
            lis.append(height)
        else:
            # Binary search to find the position to replace
            index = bisect.bisect_left(lis, height)
            lis[index] = height
    
    # Step 3: Calculate the total distance
    total_distance = 0
    for a, b in pairs:
        # Find the positions in the sorted heights array
        pos_a = bisect.bisect_left(H, a)
        pos_b = bisect.bisect_left(H, b)
        
        # Calculate the distance between the positions
        distance = abs(pos_b - pos_a)
        
        # Add the distance to the total
        total_distance += distance
    
    # Step 4: Output the result
    print(total_distance)

# Read input
N, M = map(int, input().split())
H = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(M)]

# Find and print the optimal bridge distance
find_optimal_bridge(N, M, H, pairs)
# Generator time: 28.4210 seconds