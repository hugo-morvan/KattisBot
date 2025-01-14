import math

def solve(s, t, blades):
    if s == t:
        return 0
    elif s > t:
        return -1

    def get_time(piece_size):
        time = 0
        for blade in blades:
            m, h = blade[0], blade[1]
            while piece_size > m:
                time += h
                piece_size = math.floor(piece_size / 2)
        return time

    s_time = get_time(s)
    t_time = get_time(t)
    return min(t_time - s_time, 10**6 + 1)
# Generator time: 19.4974 seconds