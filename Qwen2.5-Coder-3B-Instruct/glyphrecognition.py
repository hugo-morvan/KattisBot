import math

def shoelace_formula(points):
    n = len(points)
    area = 0.5 * abs(sum(x * y1 - y * x1 for x, y in zip(points, points[1:] + points[:1])))
    return area

def find_polygon(points, k):
    def is_inside(point):
        # Check if a point is inside the polygon using the ray casting algorithm
        crossings = 0
        for i in range(k):
            j = (i + 1) % k
            p1, p2 = points[i], points[j]
            if (p1[1] <= point[1] < p2[1]) or (p2[1] <= point[1] < p1[1]):
                if point[0] < p1[0] + (p2[0] - p1[0]) * (point[1] - p1[1]) / (p2[1] - p1[1]):
                    crossings += 1
        return crossings % 2 == 1

    def find_min_distance(points):
        min_dist = float('inf')
        min_point = None
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            if dist < min_dist:
                min_dist = dist
                min_point = point
        return min_point

    min_point = find_min_distance(points)
    angles = sorted([(math.atan2(y - min_point[1], x - min_point[0]), x, y) for x, y in points])
    polygon = [min_point]
    for angle, x, y in angles:
        while True:
            new_angle = (angle + 2 * math.pi) % (2 * math.pi)
            if not is_inside((x, y)):
                break
            polygon.append((x, y))
            angle = new_angle
    return polygon

def calculate_score(points, k):
    inner_polygon = find_polygon(points, k)
    outer_polygon = find_polygon([(-x, -y) for x, y in points], k)
    A_inner = shoelace_formula(inner_polygon)
    A_outer = shoelace_formula(outer_polygon)
    return A_inner / A_outer

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    best_k = None
    best_score = -math.inf

    for k in range(3, 9):
        score = calculate_score(points, k)
        if score > best_score:
            best_score = score
            best_k = k

    print(best_k, best_score)

if __name__ == "__main__":
    main()
# Generator time: 36.1857 seconds