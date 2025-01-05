def min_additional_spots(n, spots):
    # Convert input to list of tuples
    points = [tuple(map(int, line.split())) for line in spots]
    
    # Check for point symmetry
    point_symmetry = False
    for a in range(-20000, 20001):
        valid = True
        for x, y in points:
            if 2 * a != x + y:
                valid = False
                break
        if valid:
            point_symmetry = True
            break
    
    if point_symmetry:
        return 0
    
    # Check for line symmetry
    line_symmetry = False
    for x, y in points:
        if x == 0 and y != 0:
            line_symmetry = True
            break
        if x != 0 and y == 0:
            line_symmetry = True
            break
        if x > 0 and y > 0 and x != y:
            line_symmetry = True
            break
        if x < 0 and y < 0 and x != y:
            line_symmetry = True
            break
    
    if line_symmetry:
        # Calculate additional spots for line symmetry
        additional_points = 0
        for x, y in points:
            if x != 0 and y != 0:
                additional_points += 1
        return additional_points
    
    # If neither point nor line symmetry, add all necessary points
    return len(points)

# Read input
n = int(input())
spots = []
for _ in range(n):
    spots.append(input())

# Output the result
print(min_additional_spots(n, spots))
# Generator time: 36.3649 seconds