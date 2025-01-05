import math

def shoelace_formula(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def is_within_distance(x, y, center_x, center_y, d):
    return math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) <= d

def expand_polygon(vertices, d):
    n = len(vertices)
    new_vertices = set()
    
    # Add all original vertices
    for x, y in vertices:
        new_vertices.add((x, y))
    
    # Check for points within distance d of any vertex
    for x, y in vertices:
        for i in range(n):
            if is_within_distance(x, y, vertices[i][0], vertices[i][1], d):
                new_vertices.add(vertices[i])
    
    return list(new_vertices)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    d = int(data[1])
    g = int(data[2])
    
    vertices = []
    for _ in range(n):
        x, y = map(int, data[3 + 2 * _ : 3 + 2 * (_ + 1)])
        vertices.append((x, y))
    
    current_area = shoelace_formula(vertices)
    
    for _ in range(g):
        vertices = expand_polygon(vertices, d)
        current_area = shoelace_formula(vertices)
    
    print(f"{current_area:.3f}")

if __name__ == "__main__":
    main()
# Generator time: 30.2785 seconds