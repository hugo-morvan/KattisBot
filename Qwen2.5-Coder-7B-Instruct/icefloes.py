import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def is_point_in_polygon(point, polygon):
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

def calculate_polygon_area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2.0
    return area

def find_smallest_floe(scientists, ice_floes, d):
    min_area = float('inf')
    for floe in ice_floes:
        if is_point_in_polygon(scientists[0], floe) or is_point_in_polygon(scientists[1], floe):
            area = calculate_polygon_area(floe)
            if area < min_area and all(calculate_distance(p, q) <= d for p in scientists for q in floe):
                min_area = area
    return min_area

def main():
    N = int(input())
    results = []
    for _ in range(N):
        f, d = map(float, input().split())
        scientists = tuple(map(int, input().split() for _ in range(2)))
        ice_floes = [tuple(map(int, input().split()[1:]) for _ in range(int(input()))) for _ in range(f)]
        min_area = find_smallest_floe(scientists, ice_floes, d)
        if math.isinf(min_area):
            results.append("Scientists cannot meet")
        else:
            results.append(f"{min_area:.8f}")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 16.9509 seconds