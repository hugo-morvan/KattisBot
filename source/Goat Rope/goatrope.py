import math

def min_distance_to_house(x, y, x1, y1, x2, y2):
    # Calculate the distances from the goat's post to the four sides of the house
    dist_left = max(0, x1 - x)
    dist_right = max(0, x - x2)
    dist_top = max(0, y1 - y)
    dist_bottom = max(0, y - y2)
    
    # The minimum distance to the house is the minimum of these four distances
    min_dist = min(dist_left, dist_right, dist_top, dist_bottom)
    
    return min_dist

# Read input
x, y, x1, y1, x2, y2 = map(int, input().split())

# Calculate the minimum distance
result = min_distance_to_house(x, y, x1, y1, x2, y2)

# Print the result
print(result)