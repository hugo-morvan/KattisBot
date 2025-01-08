N = int(input())
events = []

for _ in range(N):
    s_i, t_i = map(int, input().split())
    events.append((s_i, t_i))

days_served = set()

for s_i, t_i in events:
    for day in range(s_i, t_i + 1):
        days_served.add(day)

print(len(days_served))
# Generator time: 4.4707 seconds