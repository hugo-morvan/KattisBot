n = int(input())
a = [0] * n
for i in range(1, n):
    for j in range(1, i+1):
        print(min(a[i], a[j]))

print('!', end='')
for v in sorted(a, reverse=True):
    print(v, end=' ')
# Generator time: 4.9134 seconds