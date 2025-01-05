import sys

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def orientation(p1, p2, p3):
    val = cross_product(p1, p2, p3)
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

def convex_hull(points):
    points.sort(key=lambda x: (x[0], x[1]))
    
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != 2:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != 2:
            upper.pop()
        upper.append(p)
    
    convex_hull_points = lower[:-1] + upper[:-1]
    return convex_hull_points

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    convex_hull_points = convex_hull(points)
    
    print(len(convex_hull_points))
    for point in convex_hull_points:
        print(*point)

if __name__ == "__main__":
    main()
# Generator time: 16.2740 seconds