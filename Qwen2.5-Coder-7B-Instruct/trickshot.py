import math

def calculate_collision_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.atan2(dy, dx) * 180 / math.pi

def reflect_vector(vx, vy, nx, ny):
    n = math.sqrt(nx**2 + ny**2)
    cos_theta = (nx * vx + ny * vy) / n
    sin_theta = (ny * vx - nx * vy) / n
    new_vx = 2 * cos_theta * nx - vx
    new_vy = 2 * sin_theta * ny - vy
    return new_vx, new_vy

def is_within_table(x, y, w, l):
    return 0 <= x < w and 0 <= y < l

def find_possible_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    left_hole = (0, l)
    right_hole = (w, l)

    for d in range(1, w + 1):
        for theta in range(1, 90):
            cue_ball_x = d
            cue_ball_y = h

            # Shoot the cue ball at angle theta
            vx_cue = math.cos(theta * math.pi / 180)
            vy_cue = math.sin(theta * math.pi / 180)

            # First collision with ball 1
            x, y = cue_ball_x, cue_ball_y
            while is_within_table(x, y, w, l):
                if (x - x1)**2 + (y - y1)**2 <= r**2:
                    v_theta = calculate_collision_angle(x, y, x1, y1)
                    vx_new, vy_new = reflect_vector(vx_cue, vy_cue, math.cos(v_theta * math.pi / 180), math.sin(v_theta * math.pi / 180))
                    vx_cue, vy_cue = vx_new, vy_new
                    break
                x += vx_cue
                y += vy_cue

            # Second collision with ball 2
            if not is_within_table(x, y, w, l):
                continue

            while is_within_table(x, y, w, l):
                if (x - x2)**2 + (y - y2)**2 <= r**2:
                    v_theta = calculate_collision_angle(x, y, x2, y2)
                    vx_new, vy_new = reflect_vector(vx_cue, vy_cue, math.cos(v_theta * math.pi / 180), math.sin(v_theta * math.pi / 180))
                    vx_cue, vy_cue = vx_new, vy_new
                    break
                x += vx_cue
                y += vy_cue

            # Check if ball 2 reaches the left hole
            if (x - left_hole[0])**2 + (y - left_hole[1])**2 <= r**2:
                continue

            # Third collision with ball 3
            while is_within_table(x, y, w, l):
                if (x - x3)**2 + (y - y3)**2 <= r**2:
                    v_theta = calculate_collision_angle(x, y, x3, y3)
                    vx_new, vy_new = reflect_vector(vx_cue, vy_cue, math.cos(v_theta * math.pi / 180), math.sin(v_theta * math.pi / 180))
                    vx_cue, vy_cue = vx_new, vy_new
                    break
                x += vx_cue
                y += vy_cue

            # Check if ball 3 reaches the right hole
            if (x - right_hole[0])**2 + (y - right_hole[1])**2 <= r**2:
                print(f"{d:.2f} {theta:.2f}")
                return

    print("impossible")

# Read input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(float, input().split())

# Find and print the result
find_possible_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
# Generator time: 25.2121 seconds