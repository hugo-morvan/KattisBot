import sys
from math import sqrt

def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

def point_in_polygon(point, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if point[1] > min(p1y, p2y):
            if point[1] <= max(p1y, p2y):
                if point[0] <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or point[0] <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def closest_point_on_line(p1, p2, point):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1
    t = ((point[0] - x1) * dx + (point[1] - y1) * dy) / (dx ** 2 + dy ** 2)
    if t < 0:
        return p1
    elif t > 1:
        return p2
    else:
        return (x1 + t * dx, y1 + t * dy)

def distance_between_points(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_connection(s1, s2, ice_floes, max_distance):
    for f1 in ice_floes:
        for f2 in ice_floes:
            if f1 != f2 and distance_between_points(f1[0], f2[0]) <= max_distance:
                if point_in_polygon(s1, f1) and point_in_polygon(s2, f2):
                    return True
                if point_in_polygon(f1, s1) and point_in_polygon(f2, s2):
                    return True
                if point_in_polygon(closest_point_on_line(f1[0], f1[1], s1), f2) and point_in_polygon(closest_point_on_line(f1[0], f1[1], s2), f2):
                    return True
                if point_in_polygon(f1, closest_point_on_line(f2[0], f2[1], s1)) and point_in_polygon(f2, closest_point_on_line(f2[0], f2[1], s2)):
                    return True
    return False

def solve(test_case):
    f, d = map(int, input().split())
    d = float(d)
    scientists = [tuple(map(int, input().split())) for _ in range(2)]
    ice_floes = [list(map(tuple, map(int, input().split()))) for _ in range(f)]

    min_area = float('inf')
    for i in range(f):
        for j in range(i + 1, f):
            if check_connection(scientists[0], scientists[1], [ice_floes[i]], d):
                area = polygon_area(ice_floes[i])
                if area < min_area:
                    min_area = area

    if min_area == float('inf'):
        print("Scientists cannot meet")
    else:
        print(min_area)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve(_ + 1)
# Generator time: 38.7058 seconds