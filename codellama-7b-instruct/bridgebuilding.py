n, m = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
d = {i+1:[] for i in range(n)}
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    d[a].append(b)
    d[b].append(a)
ans = 0
for i in range(1, n+1):
    if len(d[i]) == 2:
        a, b = d[i][0], d[i][1]
        ans += abs(h[b-1] - h[a-1]) + 1
print(ans)
# Generator time: 6.6599 seconds