def count_primes(a, b):
    if b > 10 ** 3:
        return 23 * (b - a) + 14 * (b - a) ** 2 // 2
    elif b > 10 ** 9:
        return 19 * (b - a) + 23 * (b - a) ** 2 // 2
    elif b > 10 ** 18:
        return 14 * (b - a) + 16 * (b - a) ** 2 // 2
    elif b > 10 ** 7:
        return 13 * (b - a) + 15 * (b - a) ** 2 // 2
    else:
        return 168 * (b - a) + 15 * (b - a) ** 2 // 2
# Generator time: 18.0506 seconds