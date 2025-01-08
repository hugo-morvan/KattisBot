from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def modular_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % m

def chinese_remainder_theorem(a, n, b, m):
    K = n * m
    p = modular_inverse(n, m)
    q = modular_inverse(m, n)
    x = (a * m * p + b * n * q) % K
    return x, K

T = int(input())
results = []

for _ in range(T):
    a, n, b, m = map(int, input().split())
    x, K = chinese_remainder_theorem(a, n, b, m)
    results.append((x, K))

for result in results:
    print(result[0], result[1])
# Generator time: 33.3384 seconds