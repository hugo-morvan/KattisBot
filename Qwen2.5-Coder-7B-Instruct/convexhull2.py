import sys

def find_convex_hull_points(n, points):
    # Sort by x-coordinate; if x-coordinates are equal, sort by y-coordinate in descending order
    points.sort(key=lambda p: (p[0], -p[1]))
    
    # Function to calculate the cross product of vectors OA and OB
    def cross_product(O, A, B):
        return (A[0] - O[0]) * (B[1] - O[1]) - (A[1] - O[1]) * (B[0] - O[0])
    
    # Build the lower hull
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    
    # Build the upper hull
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    
    # The convex hull is the concatenation of lower_hull and upper_hull, minus the first and last points (they are repeated)
    convex_hull = lower_hull[:-1] + upper_hull[:-1]
    
    return len(convex_hull), convex_hull

# Read input
n = int(input())
points = []
for _ in range(n):
    x, y, is_on_hull = input().split()
    points.append((int(x), int(y)))

# Find the number of points on the convex hull and the points themselves
m, convex_hull = find_convex_hull_points(n, points)

# Output the result
print(m)
for x, y in convex_hull:
    print(x, y)
# Generator time: 12.5269 seconds