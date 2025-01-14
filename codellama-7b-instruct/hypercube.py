import math
n = int(input())
a = list(bin(int("0b" + input(), 2))[3:])
b = list(bin(int("0b" + input(), 2))[3:])
i = j = 0
while a[i] == b[j]:
    i += 1
    j += 1
if i != n or j != n:
    print((i + j) // 2)
else:
    print(math.ceil((n * (n + 1)) / 2 - math.floor((a[i] - b[j]) / (1 << (n - 1))) * math.comb(n, 2)))
# Generator time: 5.8476 seconds