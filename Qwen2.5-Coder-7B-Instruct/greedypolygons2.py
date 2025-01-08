import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area_of_polygon(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x1 * y2 - x2 * y1 for x1, y1, x2, y2 in zip(vertices, vertices[1:] + vertices[:1])))
    return area

def expand_polygon(polygon, d):
    new_vertices = []
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        dist = distance(x1, y1, x2, y2)
        angle = math.atan2(y2 - y1, x2 - x1)
        for a in range(360):
            radian = math.radians(a)
            new_x = x1 + (d / dist) * (math.cos(angle + radian) * x2 - math.sin(angle + radian) * y2)
            new_y = y1 + (d / dist) * (math.sin(angle + radian) * x2 + math.cos(angle + radian) * y2)
            if not any(distance(new_x, new_y, px, py) < d for px, py in new_vertices):
                new_vertices.append((new_x, new_y))
    return new_vertices

def main():
    n, d, g = map(int, input().split())
    vertices = [tuple(map(int, input().split())) for _ in range(n)]
    
    for _ in range(g):
        vertices = expand_polygon(vertices, d)
    
    area = area_of_polygon(vertices)
    print(f"{area:.3f}")

if __name__ == "__main__":
    main()
# Generator time: 12.8098 seconds