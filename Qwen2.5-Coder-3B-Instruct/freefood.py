N = int(input())
events = []
for _ in range(N):
    s, t = map(int, input().split())
    events.append((s, t))

days_served = set()
for s, t in events:
    days_served.update(range(s, t + 1))

print(len(days_served))
# Generator time: 3.2882 seconds