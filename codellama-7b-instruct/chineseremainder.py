import math

def solve(T):
    for _ in range(T):
        (a, n, b, m) = tuple(map(int, input().split()))
        gcd = math.gcd(n,m)
        print((b*n+a)%n*m//gcd,(b*n+a)%n*m//gcd)
# Generator time: 9.7625 seconds