import sys
from math import sqrt

def distance(x1, y1, z1, x2, y2, z2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def main():
    N = int(input().strip())
    ships = []
    for _ in range(N):
        x, y, z, r = map(int, input().strip().split())
        ships.append((x, y, z, r))
    
    M = int(input().strip())
    bombs = []
    for _ in range(M):
        x, y, z, r = map(int, input().strip().split())
        bombs.append((x, y, z, r))
    
    surviving_ships = N
    
    for bomb in bombs:
        bomb_x, bomb_y, bomb_z, bomb_r = bomb
        for i in range(N):
            ship_x, ship_y, ship_z, ship_r = ships[i]
            if distance(bomb_x, bomb_y, bomb_z, ship_x, ship_y, ship_z) <= bomb_r + ship_r:
                surviving_ships -= 1
                break
    
    print(surviving_ships)

if __name__ == "__main__":
    main()
# Generator time: 12.6009 seconds