def find_path(x_s, y_s, x_t, y_t, x_p, y_p):
    # Determine the direction from start to target
    dx = x_t - x_s
    dy = y_t - y_s
    
    # Calculate the path avoiding the pool
    if dx > 0 and dy > 0:
        path = [(x_s + 1, y_s), (x_s + 1, y_p), (x_t, y_p)]
    elif dx > 0 and dy < 0:
        path = [(x_s + 1, y_s), (x_s + 1, y_p), (x_t, y_p)]
    elif dx < 0 and dy > 0:
        path = [(x_s - 1, y_s), (x_s - 1, y_p), (x_t, y_p)]
    elif dx < 0 and dy < 0:
        path = [(x_s - 1, y_s), (x_s - 1, y_p), (x_t, y_p)]
    else:
        # If the target is directly above or below
        if dy > 0:
            path = [(x_s, y_s + 1), (x_s, y_p), (x_t, y_p)]
        else:
            path = [(x_s, y_s - 1), (x_s, y_p), (x_t, y_p)]
    
    return len(path) - 2, path[1:-1]

# Read input
x_s, y_s = map(int, input().split())
x_t, y_t = map(int, input().split())
x_p, y_p = map(int, input().split())

# Find and print the path
N, points = find_path(x_s, y_s, x_t, y_t, x_p, y_p)
print(N)
for point in points:
    print(point[0], point[1])
# Generator time: 12.5361 seconds