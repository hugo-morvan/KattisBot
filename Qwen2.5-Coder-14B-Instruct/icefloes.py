import sys
from typing import List, Tuple

def polygon_area(vertices: List[Tuple[int, int]]) -> float:
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def point_in_polygon(point: Tuple[int, int], polygon: List[Tuple[int, int]]) -> bool:
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def is_close(polygon1: List[Tuple[int, int]], polygon2: List[Tuple[int, int]], d: float) -> bool:
    for point in polygon1:
        if min((point[0] - px) ** 2 + (point[1] - py) ** 2 for px, py in polygon2) <= d ** 2:
            return True
    for point in polygon2:
        if min((point[0] - px) ** 2 + (point[1] - py) ** 2 for px, py in polygon1) <= d ** 2:
            return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    
    for _ in range(N):
        f = int(data[index])
        d = float(data[index + 1])
        index += 2
        
        scientists = []
        for _ in range(2):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            scientists.append((x, y))
        
        polygons = []
        areas = []
        for _ in range(f):
            v = int(data[index])
            index += 1
            polygon = [(int(data[index + 2 * i]), int(data[index + 2 * i + 1])) for i in range(v)]
            index += 2 * v
            polygons.append(polygon)
            areas.append(polygon_area(polygon))
        
        reachable = [False] * f
        queue = []
        for i, polygon in enumerate(polygons):
            if any(point_in_polygon(scientist, polygon) for scientist in scientists):
                reachable[i] = True
                queue.append(i)
        
        while queue:
            current = queue.pop(0)
            for next_floe in range(f):
                if not reachable[next_floe] and is_close(polygons[current], polygons[next_floe], d):
                    reachable[next_floe] = True
                    queue.append(next_floe)
        
        if all(reachable):
            print(min(areas))
        else:
            print("Scientists cannot meet")

if __name__ == "__main__":
    main()
# Generator time: 101.5224 seconds