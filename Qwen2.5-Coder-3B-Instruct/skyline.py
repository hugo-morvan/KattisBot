import math

def visible_area(x1, y1, x2, y2):
    # Calculate the area of the trapezoid
    base1 = x2 - x1
    height = y2 - y1
    area = 0.5 * (base1 + height) * height
    
    # Calculate the visible area
    # We need to consider the overlap with other buildings
    # For simplicity, we assume that the buildings are sorted by distance
    # and the first building is always visible.
    
    # For each subsequent building, calculate the overlap
    visible_area = area
    for i in range(1, len(buildings)):
        xi, yi, xi2, yi2 = buildings[i]
        
        # Calculate the intersection of the two trapezoids
        # Find the intersection points of the top and bottom edges
        if yi > yi2:
            y_top = yi
            y_bottom = yi2
        else:
            y_top = yi2
            y_bottom = yi
        
        # Calculate the intersection of the left edge
        x_left = max(xi, x1)
        
        # Calculate the intersection of the right edge
        x_right = min(xi2, x2)
        
        # If there is no intersection, the entire area is visible
        if x_right <= x_left:
            continue
        
        # Calculate the length of the intersecting bases
        base1 = x_right - x_left
        base2 = x2 - xi
        
        # Calculate the height of the intersecting trapezoid
        height = y_top - y_bottom
        
        # Calculate the area of the intersecting trapezoid
        intersected_area = 0.5 * (base1 + height) * height
        
        # Subtract the intersected area from the total area
        visible_area -= intersected_area
    
    return visible_area

# Read input
n = int(input())
buildings = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    buildings.append((x1, y1, x2, y2))

# Calculate and print the visible area for each building
for i in range(n):
    visible_area = visible_area(*buildings[i])
    print(f"{visible_area:.6f}")
# Generator time: 30.2729 seconds