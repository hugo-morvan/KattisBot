def find_path(x_s, y_s, x_t, y_t, x_p, y_p):
    # Determine the direction of movement
    dx = x_t - x_s
    dy = y_t - y_s
    
    # Check if the point (x_p, y_p) is on the border of the pool
    if (x_p == x_l or x_p == x_r or y_p == y_l or y_p == y_r):
        # If it is on the border, we need to move around the pool
        if x_p == x_l:
            # Move horizontally to the left until we reach the left border of the pool
            while x_s != x_l:
                x_s -= 1
                print(x_s, y_s)
        elif x_p == x_r:
            # Move horizontally to the right until we reach the right border of the pool
            while x_s != x_r:
                x_s += 1
                print(x_s, y_s)
        elif y_p == y_l:
            # Move vertically upwards until we reach the top border of the pool
            while y_s != y_l:
                y_s += 1
                print(x_s, y_s)
        else:
            # Move vertically downwards until we reach the bottom border of the pool
            while y_s != y_r:
                y_s -= 1
                print(x_s, y_s)
    else:
        # If it is not on the border, we can simply move directly to the end point
        print(x_t, y_t)

# Read input
x_s, y_s = map(int, input().split())
x_t, y_t = map(int, input().split())
x_p, y_p = map(int, input().split())

# Assume the pool boundaries are given as input (this part is not provided in the problem statement)
x_l, y_l, x_r, y_r = map(int, input().split())

# Find and print the path
find_path(x_s, y_s, x_t, y_t, x_p, y_p)
# Generator time: 19.0222 seconds