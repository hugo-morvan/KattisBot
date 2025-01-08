def max_additional_birds(l, d, n, positions):
    # Add the minimum distance from the poles to the positions list
    positions = sorted([6] + positions + [l - 6])
    
    # Calculate the maximum number of additional birds that can sit on the wire
    additional_birds = 0
    for i in range(1, len(positions)):
        gap = positions[i] - positions[i-1]
        if gap > d:
            additional_birds += (gap - d) // d
    
    return additional_birds

# Read input
l, d, n = map(int, input().split())
positions = [int(input()) for _ in range(n)]

# Output the result
print(max_additional_birds(l, d, n, positions))
# Generator time: 23.7217 seconds