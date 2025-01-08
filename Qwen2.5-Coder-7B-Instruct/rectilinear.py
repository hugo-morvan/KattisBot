def can_form_rectilinear_polygon(points):
    if len(points) < 4:
        return False
    
    # Separate points by x and y coordinates
    x_points = sorted(set(point[0] for point in points))
    y_points = sorted(set(point[1] for point in points))
    
    # Check if there are enough distinct x and y coordinates
    if len(x_points) < 2 or len(y_points) < 2:
        return False
    
    # Construct the rectilinear polygon
    polygon = []
    for x in x_points:
        polygon.append((x, y_points[0]))
    for y in y_points[1:]:
        polygon.append((x_points[-1], y))
    for x in reversed(x_points[:-1]):
        polygon.append((x, y_points[-1]))
    for y in reversed(y_points[1:-1]):
        polygon.append((x_points[0], y))
    
    # Check if the polygon passes through all given points
    return set(polygon) == set(points)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    results = []
    
    num_cases = int(data[index])
    index += 1
    
    for _ in range(num_cases):
        n = int(data[index])
        index += 1
        
        points = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            points.append((x, y))
        
        if can_form_rectilinear_polygon(points):
            results.append(len(polygon))
        else:
            results.append(-1)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 12.2317 seconds