import sys

def orientation(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull_sort(points):
    n = len(points)
    if n < 3:
        return points

    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0] or (points[i][0] == points[l][0] and points[i][1] < points[l][1]):
            l = i

    hull = []
    p = l

    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for r in range((p + 2) % n, (p + n) % n):
            if orientation(points[p], points[q], points[r]) == 2:
                q = r

        p = q

        if p == l:
            break

    return hull

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    points = []

    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        is_hull = data[index + 2]
        if is_hull == 'Y':
            points.append((x, y))
        index += 3

    hull_points = convex_hull_sort(points)

    print(len(hull_points))
    for point in hull_points:
        print(point[0], point[1])

if __name__ == "__main__":
    main()
# Generator time: 53.4256 seconds