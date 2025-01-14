import math

def get_impossible_prices(a, b, t):
    res = 0
    for i in range(int(math.ceil(a)), int(math.floor(b))):
        if round(i * (1 + t/100), 2) > round(i*(1+t/100)+0.01, 2):
            res += 1
    return res

N = int(input())
for _ in range(N):
    a, b, t = map(float, input().split(' '))
    print(get_impossible_prices(a, b, t))
# Generator time: 6.2942 seconds