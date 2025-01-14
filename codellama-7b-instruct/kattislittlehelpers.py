import math
from collections import deque

w, h, c, t = map(int, input().split())
grid = [list(input()) for _ in range(h)]
locations = []
for i in range(t):
    x_i, y_i = map(int, input().split())
    locations.append([x_i-1,y_i-1])

if c > (w*h)-2:
    print("impossible")
    exit()

queue = deque(locations)
visited = set()
steps = 0
while queue:
    steps += 1
    for _ in range(c):
        x, y = queue.popleft()
        visited.add((x,y))
        for i in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if 0 <= i[0] < w and 0 <= i[1] < h and grid[i[1]][i[0]] != "#" and i not in visited:
                queue.append(i)

print(steps)
# Generator time: 8.8190 seconds