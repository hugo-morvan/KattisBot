def can_form_rectilinear_polygon(points):
    # Sort points by x-coordinate, and then by y-coordinate if x-coordinates are equal
    points.sort()

    # Check if consecutive points have either the same x or y coordinate
    for i in range(len(points) - 1):
        if points[i][0] != points[i + 1][0] and points[i][1] != points[i + 1][1]:
            return -1

    # If we can form a rectilinear polygon, calculate its perimeter
    perimeter = 0
    for i in range(len(points) - 1):
        if points[i][0] == points[i + 1][0]:
            # Vertical edge
            perimeter += abs(points[i][1] - points[i + 1][1])
        else:
            # Horizontal edge
            perimeter += abs(points[i][0] - points[i + 1][0])

    # Add the last edge to close the polygon
    if points[0][0] == points[-1][0]:
        perimeter += abs(points[0][1] - points[-1][1])
    else:
        perimeter += abs(points[0][0] - points[-1][0])

    return perimeter

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    num_cases = int(data[index])
    index += 1

    results = []

    for _ in range(num_cases):
        n = int(data[index])
        index += 1

        points = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            points.append((x, y))
            index += 2

        result = can_form_rectilinear_polygon(points)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 51.8991 seconds