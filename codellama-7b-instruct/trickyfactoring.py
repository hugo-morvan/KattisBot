def b_values(a, c):
    for b in range(1, int((c ** 0.5) / a) + 1):
        if (c - b**2 * a) % a == 0:
            return (b+1)
    return 0
# Generator time: 3.8963 seconds