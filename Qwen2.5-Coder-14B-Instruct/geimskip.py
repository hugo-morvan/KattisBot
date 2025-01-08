import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def is_exploded(ship, bomb):
    d = distance(ship[:3], bomb[:3])
    return d <= ship[3] + bomb[3]

N = int(input())
ships = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(M)]

exploded_ships = set()

for i in range(N):
    for j in range(M):
        if is_exploded(ships[i], bombs[j]):
            exploded_ships.add(i)

surviving_ships = N - len(exploded_ships)

print(surviving_ships)
# Generator time: 29.0547 seconds