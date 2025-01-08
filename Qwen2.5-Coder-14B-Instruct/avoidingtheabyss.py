def find_path(x_s, y_s, x_t, y_t, x_p, y_p):
    # Calculate the midpoints of the start and end points
    mid_x = (x_s + x_t) // 2
    mid_y = (y_s + y_t) // 2
    
    # Check if the midpoint is inside the pool
    if (min(x_s, x_t) < mid_x < max(x_s, x_t)) and (min(y_s, y_t) < mid_y < max(y_s, y_t)):
        # If the midpoint is inside the pool, we need to adjust our path
        if x_p == x_s or x_p == x_t:
            # Vertical adjustment
            mid_x = x_s + (x_t - x_s) // 2
        else:
            # Horizontal adjustment
            mid_y = y_s + (y_t - y_s) // 2
    
    # Print the path
    print(1)
    print(mid_x, mid_y)

# Read input
x_s, y_s = map(int, input().split())
x_t, y_t = map(int, input().split())
x_p, y_p = map(int, input().split())

# Find and print the path
find_path(x_s, y_s, x_t, y_t, x_p, y_p)
# Generator time: 38.3166 seconds