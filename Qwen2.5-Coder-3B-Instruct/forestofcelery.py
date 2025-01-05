import sys
from itertools import combinations

def orientation(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

def convex_hull(points):
    if len(points) < 3:
        return points
    
    # Find the leftmost point
    leftmost = min(points, key=lambda p: (p[0], p[1]))
    
    # Sort points by polar angle with respect to the leftmost point
    def polar_angle(p):
        return (math.atan2(p[1] - leftmost[1], p[0] - leftmost[0]), p)
    
    sorted_points = sorted(points, key=polar_angle)
    
    # Build the convex hull
    hull = []
    for p in sorted_points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)
    
    return hull

def is_inside_polygon(polygon, point):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if point[1] > min(p1y, p2y):
            if point[1] <= max(p1y, p2y):
                if point[0] <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or point[0] <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def find_smallest_polygon(N, vertices, K, sightings):
    hull = convex_hull(vertices)
    min_vertices = N
    
    for r in range(2, N + 1):
        for subset in combinations(hull, r):
            if all(is_inside_polygon(subset, sight) for sight in sightings):
                min_vertices = min(min_vertices, r)
                break
    
    return min_vertices

if __name__ == "__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    N = data[0]
    vertices = [(data[i], data[i + 1]) for i in range(1, 2 * N + 1, 2)]
    K = data[2 * N + 1]
    sightings = [(data[i], data[i + 1]) for i in range(2 * N + 2, 2 * N + 2 + K * 2, 2)]
    
    result = find_smallest_polygon(N, vertices, K, sightings)
    print(result)
# Generator time: 43.6047 seconds