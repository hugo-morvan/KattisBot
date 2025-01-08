def find_min_additional_spots(n, spots):
    from collections import defaultdict
    
    # Function to calculate the distance between two points
    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    
    # Check for point symmetry
    point_symmetry = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            center_x = (spots[i][0] + spots[j][0]) / 2
            center_y = (spots[i][1] + spots[j][1]) / 2
            key = (center_x, center_y)
            point_symmetry[key] += 1
    
    # Find the maximum number of symmetric pairs around any point
    max_point_pairs = max(point_symmetry.values())
    
    # Check for line symmetry
    line_symmetry = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            if spots[j][0] == spots[i][0]:  # Vertical line
                key = (spots[i][0], 'v')
            else:
                slope = (spots[j][1] - spots[i][1]) / (spots[j][0] - spots[i][0])
                intercept = spots[i][1] - slope * spots[i][0]
                key = (slope, intercept)
            line_symmetry[key] += 1
    
    # Find the maximum number of symmetric pairs across any line
    max_line_pairs = max(line_symmetry.values())
    
    # The minimum additional spots needed is n minus the maximum symmetric pairs found
    return n - max(max_point_pairs, max_line_pairs)

# Read input
n = int(input().strip())
spots = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Output the result
print(find_min_additional_spots(n, spots))
# Generator time: 52.8286 seconds