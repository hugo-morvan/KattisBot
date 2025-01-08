import sys
from math import sqrt

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def expand_polygon(polygon, d):
    expanded_points = set()
    for x in range(min(p[0] for p in polygon) - d, max(p[0] for p in polygon) + d + 1):
        for y in range(min(p[1] for p in polygon) - d, max(p[1] for p in polygon) + d + 1):
            if any(distance((x, y), p) <= d for p in polygon):
                expanded_points.add((x, y))
    return convex_hull(expanded_points)

def polygon_area(polygon):
    n = len(polygon)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    d = int(data[idx + 1])
    g = int(data[idx + 2])
    idx += 3
    
    points = []
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        points.append((x, y))
        idx += 2
    
    polygon = convex_hull(points)
    
    for _ in range(g):
        polygon = expand_polygon(polygon, d)
    
    area = polygon_area(polygon)
    print(f"{area:.3f}")

if __name__ == "__main__":
    main()
# Generator time: 75.5224 seconds