import math

def is_collision_possible(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def reflect_vector(v, n):
        dot = 2 * (v[0] * n[0] + v[1] * n[1])
        return [v[0] - dot * n[0], v[1] - dot * n[1]]

    def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Check if ball 2 and ball 3 are in the top left and right holes respectively
    if not (0 <= x2 < w and y2 == l) or not (w - r <= x3 < w and y3 == l):
        return "impossible"

    # Calculate the direction vector from cue ball to ball 1
    for d in range(w + 1):
        for theta in range(0, 361):
            dx = math.cos(math.radians(theta))
            dy = math.sin(math.radians(theta))
            v_cue = [dx, dy]

            # Position of the cue ball
            x_cue = d
            y_cue = h

            if not (r <= x_cue <= w - r and r <= y_cue <= l - r):
                continue

            # Check collision with ball 1
            v_b1 = [0, 0]
            v_b2 = [0, 0]
            v_b3 = [0, 0]

            if distance(x_cue, y_cue, x1, y1) <= 2 * r:
                v_b1 = [(x1 - x_cue), (y1 - y_cue)]
                norm_b1 = math.sqrt(v_b1[0] ** 2 + v_b1[1] ** 2)
                v_b1 = [v_b1[0] / norm_b1, v_b1[1] / norm_b1]
                v_cue = reflect_vector(v_cue, v_b1)

            # Check collision with ball 2
            if distance(x1 + v_b1[0], y1 + v_b1[1], x2, y2) <= 2 * r:
                v_b2 = [(x2 - (x1 + v_b1[0])), (y2 - (y1 + v_b1[1]))]
                norm_b2 = math.sqrt(v_b2[0] ** 2 + v_b2[1] ** 2)
                v_b2 = [v_b2[0] / norm_b2, v_b2[1] / norm_b2]
                v_b1 = reflect_vector(v_b1, v_b2)

            # Check collision with ball 3
            if distance(x1 + v_b1[0], y1 + v_b1[1], x3, y3) <= 2 * r:
                v_b3 = [(x3 - (x1 + v_b1[0])), (y3 - (y1 + v_b1[1]))]
                norm_b3 = math.sqrt(v_b3[0] ** 2 + v_b3[1] ** 2)
                v_b3 = [v_b3[0] / norm_b3, v_b3[1] / norm_b3]
                v_b2 = reflect_vector(v_b2, v_b3)

            # Check if ball 2 and ball 3 are in the correct holes
            if (0 <= x2 < w and y2 == l) and (w - r <= x3 < w and y3 == l):
                return f"{d:.2f} {theta:.2f}"

    return "impossible"

# Read input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Output result
print(is_collision_possible(w, l, r, x1, y1, x2, y2, x3, y3, h))
# Generator time: 119.0984 seconds