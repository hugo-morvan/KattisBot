import sys

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def is_inside_polygon(polygon, point):
    n = len(polygon)
    extreme = (10**9 + 1, point[1])
    count = 0
    i = 0
    while True:
        next = (i + 1) % n
        if orientation(polygon[i], polygon[next], point) == 0:
            return False
        elif orientation(polygon[i], polygon[next], extreme) != orientation(point, polygon[next], extreme):
            count += 1
        i = next
        if i == 0:
            break
    return count % 2 != 0

def smallest_polygon_vertices(N, A, K, Celery_points):
    min_vertices = N
    for i in range(N):
        for j in range(i + 1, N):
            polygon = [A[i], A[j]]
            valid = True
            for point in Celery_points:
                if not is_inside_polygon(polygon, point):
                    valid = False
                    break
            if valid:
                min_vertices = min(min_vertices, len(polygon))
    return min_vertices

def main():
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    K = int(input())
    Celery_points = [tuple(map(int, input().split())) for _ in range(K)]
    print(smallest_polygon_vertices(N, A, K, Celery_points))

if __name__ == "__main__":
    main()
# Generator time: 52.5723 seconds