def is_rectilinear_polygon_possible(points):
    # Check if the points have unique x and y coordinates
    x_coords = set()
    y_coords = set()
    for x, y in points:
        if x in x_coords or y in y_coords:
            return False
        x_coords.add(x)
        y_coords.add(y)
    
    # Check if the points can be connected in a rectilinear manner
    if len(points) < 4:
        return False
    
    # Sort points by x and then by y
    points.sort(key=lambda p: (p[0], p[1]))
    
    # Check if the points can be connected in a rectilinear manner
    for i in range(len(points)):
        if i > 0 and points[i][0] == points[i-1][0]:
            continue
        if i < len(points) - 1 and points[i][1] == points[i+1][1]:
            continue
    
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    del data[:1]
    
    for _ in range(num_cases):
        n = int(data[0])
        del data[:1]
        
        points = [(int(data[i]), int(data[i+1])) for i in range(0, 2*n, 2)]
        
        if is_rectilinear_polygon_possible(points):
            print(n)
        else:
            print(-1)

if __name__ == "__main__":
    main()
# Generator time: 28.0092 seconds