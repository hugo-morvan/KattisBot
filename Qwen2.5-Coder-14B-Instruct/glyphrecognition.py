import math

def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def fit_polygon(points, k):
    points.sort(key=lambda p: math.atan2(p[1], p[0]))
    angles = [math.atan2(p[1], p[0]) for p in points]
    
    min_angle = min(angles)
    max_angle = max(angles)
    
    if max_angle - min_angle < 2 * math.pi:
        angles.append(max_angle + 2 * math.pi)
    
    vertices_inner = []
    vertices_outer = []
    
    for angle in angles:
        radian = (angle - min_angle) / k * 2 * math.pi
        x_inner = math.cos(radian)
        y_inner = math.sin(radian)
        x_outer = math.cos(radian + 2 * math.pi / k)
        y_outer = math.sin(radian + 2 * math.pi / k)
        
        vertices_inner.append((x_inner, y_inner))
        vertices_outer.append((x_outer, y_outer))
    
    return polygon_area(vertices_inner), polygon_area(vertices_outer)

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    best_k = 0
    best_score = -1.0
    
    for k in range(3, 9):
        inner_area, outer_area = fit_polygon(points, k)
        score = inner_area / outer_area
        
        if score > best_score:
            best_score = score
            best_k = k
    
    print(best_k, best_score)

if __name__ == "__main__":
    main()
# Generator time: 53.8247 seconds