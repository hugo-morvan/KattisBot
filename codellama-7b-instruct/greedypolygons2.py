import math
import collections
import itertools

def polygon_area(points):
    return abs(sum(a * b for a, b in zip(points[:-1], points[1:]))) / 2

def landgrab_polygon(points, d, g):
    if len(points) == 3:
        return polygon_area(points) + d
    new_points = [point for point in points if abs(point[0]) <= d or abs(point[1]) <= d]
    return max(polygon_area(new_points), landgrab_polygon(new_points, d, g - 1))

def solve(n, d, g):
    points = [[int(x), int(y)] for x, y in itertools.zip_longest(*[input().split() for _ in range(n)])]
    return landgrab_polygon(points, d, g)
# Generator time: 7.0489 seconds