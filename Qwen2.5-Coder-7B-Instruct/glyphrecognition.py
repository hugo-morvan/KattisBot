import math

def calculate_score(k, points):
    def polygon_area(vertices):
        n = len(vertices)
        area = 0
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            area += x1 * y2 - y1 * x2
        return abs(area) / 2.0

    def fit_polygon(points, k, direction):
        from scipy.spatial import ConvexHull
        hull = ConvexHull(points)
        vertices = [(points[i][0], points[i][1]) for i in hull.vertices]
        
        if direction == 'inner':
            # Find the largest polygon inside the convex hull
            while len(vertices) > k:
                hull = ConvexHull(vertices[:k])
                vertices = [(vertices[i][0], vertices[i][1]) for i in hull.vertices]
        elif direction == 'outer':
            # Find the smallest polygon outside the convex hull
            new_points = points + [(0, 0)]
            hull = ConvexHull(new_points)
            vertices = [(new_points[i][0], new_points[i][1]) for i in hull.vertices]
        
        return polygon_area(vertices)

    inner_score = fit_polygon(points, k, 'inner')
    outer_score = fit_polygon(points, k, 'outer')
    return inner_score / outer_score

def find_optimal_glyph(points):
    n = len(points)
    scores = {}
    
    for k in range(3, 9):
        score = calculate_score(k, points)
        if score not in scores or score > max(scores.values()):
            scores[score] = k
    
    optimal_k = max(scores.values())
    optimal_score = scores[optimal_k]
    
    return optimal_k, optimal_score

def main():
    n = int(input().strip())
    points = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        points.append((x, y))
    
    optimal_k, optimal_score = find_optimal_glyph(points)
    print(optimal_k, optimal_score)

if __name__ == "__main__":
    main()
# Generator time: 13.7539 seconds