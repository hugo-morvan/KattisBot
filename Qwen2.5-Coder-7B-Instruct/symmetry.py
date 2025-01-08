def find_min_additional_spots(spots):
    n = len(spots)
    
    # Function to calculate the midpoint between two points
    def midpoint(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
    # Function to check if a point is symmetric about a given line
    def is_symmetric(point, line_point, line_slope):
        x1, y1 = point
        x2, y2 = line_point
        m = line_slope
        
        if m == float('inf'):
            return x1 == x2
        
        b = y2 - m * x2
        y_pred = m * x1 + b
        
        return abs(y1 - y_pred) < 1e-9
    
    # Function to check if a point is symmetric about a given point
    def is_symmetric_point(point, center):
        x1, y1 = point
        xc, yc = center
        return (2 * xc - x1, 2 * yc - y1) in spots
    
    # Check for symmetry across lines
    min_additional_spots_line = n
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = spots[i], spots[j]
            if p1[0] == p2[0]:
                line_slope = float('inf')
            else:
                line_slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
            
            mid = midpoint(p1, p2)
            additional_spots = 0
            for k in range(n):
                if not is_symmetric(spots[k], mid, line_slope) and spots[k] != p1 and spots[k] != p2:
                    additional_spots += 1
            
            min_additional_spots_line = min(min_additional_spots_line, additional_spots)
    
    # Check for symmetry about points
    min_additional_spots_point = n
    for i in range(n):
        center = spots[i]
        additional_spots = 0
        for k in range(n):
            if not is_symmetric_point(spots[k], center) and spots[k] != center:
                additional_spots += 1
        
        min_additional_spots_point = min(min_additional_spots_point, additional_spots)
    
    return min(min_additional_spots_line, min_additional_spots_point)

# Read input
n = int(input())
spots = [tuple(map(int, input().split())) for _ in range(n)]

# Find and print the minimum number of additional spots needed
print(find_min_additional_spots(spots))
# Generator time: 18.0828 seconds