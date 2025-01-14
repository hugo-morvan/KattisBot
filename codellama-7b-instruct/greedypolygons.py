for _ in range(int(input())):
    n, l, d, g = map(int, input().split())
    area = (n * l ** 2) / 2
    for i in range(g):
        area += (l + d) ** 2
    print(area)
# Generator time: 10.3500 seconds