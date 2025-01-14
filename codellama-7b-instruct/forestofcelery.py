import math
import collections
input()
n=int(input())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
k=int(input())
celery=list(map(lambda x:(x[0],x[1]), map(int, input().split())))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, p2):
        return (self.x + p2.x, self.y + p2.y)
    
    def __sub__(self, p2):
        return (self.x - p2.x, self.y - p2.y)
    
    def __mul__(self, a):
        return (a*self.x, a*self.y)
    
    def __eq__(self, p2):
        return self.x == p2.x and self.y == p2.y
    
    def __hash__(self):
        return hash((self.x, self.y))

def polygon(vertices):
    n = len(vertices)
    for i in range(n+1):
        yield vertices[i%n]

def intersect_line_segments(p1, p2, q1, q2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = q1.x, q1.y
    x4, y4 = q2.x, q2.y
    
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(denom) < 0.00001: # parallel line segments
        return None
    
    a = ((x3-x4)*(y1-y3)-(y3-y4)*(x1-x3))/denom
    b = ((x2-x1)*(y1-y3)-(y1-y2)*(x1-x2))/denom
    
    if not (0 <= a <= 1 and 0 <= b <= 1): # intersection outside line segments
        return None
    x = x1 + a*(x2-x1)
    y = y1 + a*(y2-y1)
    return Point(int(round(x)), int(round(y)))
    
def contains_point(polygon, p):
    n = len(polygon)
    inside = False
    for i in range(n+1):
        a = polygon[i%n] - p
        b = polygon[(i+1)%n] - p
        
        if a.y*b.x > a.x*b.y:
            continue
        
        if 0 <= b.y*a.x-b.x*a.y < 0.00001: # point on line segment
            return None
        
        if inside:
            return False
        else:
            inside = True
    
    return inside

def contains_polygon(polygon, other):
    for p in other:
        if not contains_point(polygon, p):
            return False
    return True
    
def is_inside_polygon(polygon, point):
    n = len(polygon)
    for i in range(n+1):
        a = polygon[i%n] - point
        b = polygon[(i+1)%n] - point
        
        if a.y*b.x > a.x*b.y:
            continue
        
        return None
    
    return True
    
def is_polygon_inside(polygon, other):
    for p in polygon:
        if not contains_point(other, p):
            return False
    return True


# initialize the first convex hull
hull = []
for i in range(n):
    while len(hull) >= 2 and cross(hull[-2], hull[-1], vertices[i]) <= 0:
        hull.pop()
    hull.append(vertices[i])
    
# sort points by angle with previous point
angle = lambda p, q: math.atan2(q.y-p.y, q.x-p.x)
ordered_points = sorted([Point(-10**9, -10**9), Point(10**9, 10**9)], key=lambda p: angle(hull[-1], p)) + vertices

# compute the convex hull using Jarvis' march
while len(hull) < n:
    point = ordered_points.pop()
    while contains_point(hull, point):
        point = ordered_points.pop()
    
    hull.append(point)

# find the polygon with minimum number of vertices inside Alexa Forest
polygon = []
for p in hull:
    if is_inside_polygon(polygon, p):
        polygon.append(p)

# check if Celery is strictly inside a polygon $Z$
best_polygon = None
best_vertices = -1
for p in celery:
    for z in polygons:
        if contains_point(z, p):
            vertices = len(z)
            if best_vertices == -1 or vertices < best_vertices:
                best_polygon = z
                best_vertices = vertices
            break

# find the smallest polygon $Z$ with minimum number of vertices
smallest_polygon = None
minimum_vertices = 10**5 + 1
for p in polygons:
    if len(p) < minimum_vertices:
        smallest_polygon = p
        minimum_vertices = len(p)
        
# output the answer
print(len(smallest_polygon))
# Generator time: 35.1845 seconds