v = int(input())
n = int(input())

roads = []
for _ in range(n):
    road, max_speed = input().split()
    max_speed = int(max_speed)
    roads.append((road, max_speed))

for road, max_speed in roads:
    if v <= max_speed:
        print(f"{road} opin")
    else:
        print(f"{road} lokud")