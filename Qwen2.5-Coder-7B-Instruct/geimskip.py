import math

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

N = int(input())
ships = []
for _ in range(N):
    x, y, z, r = map(int, input().split())
    ships.append((x, y, z, r))

M = int(input())
bombs = []
for _ in range(M):
    x, y, z, r = map(int, input().split())
    bombs.append((x, y, z, r))

surviving_ships = []

for ship in ships:
    x_s, y_s, z_s, r_s = ship
    if all(distance(x_s, y_s, z_s, x_b, y_b, z_b) > r_s + r_b for x_b, y_b, z_b, r_b in bombs):
        surviving_ships.append(ship)

print(len(surviving_ships))
# Generator time: 8.1717 seconds