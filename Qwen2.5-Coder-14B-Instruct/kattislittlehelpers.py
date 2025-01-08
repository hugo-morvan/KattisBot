import sys
from collections import deque

def bfs(start, grid):
    w, h = len(grid[0]), len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    distance = [[-1] * w for _ in range(h)]
    queue = deque([start])
    distance[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '#' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return distance

def min_steps(w, h, c, t, grid, tasks):
    start = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'K':
                start = (i, j)
                break
        if start:
            break

    distances = [bfs(start, grid)]
    for x, y in tasks:
        distances.append(bfs((x - 1, y - 1), grid))

    dp = [[[float('inf')] * t for _ in range(c)] for __ in range(t)]
    for i in range(c):
        dp[0][i][0] = distances[0][tasks[0][0] - 1][tasks[0][1] - 1]

    for k in range(1, t):
        for i in range(c):
            for j in range(c):
                if dp[k - 1][i][k - 1] != float('inf'):
                    dp[k][j][k] = min(dp[k][j][k], dp[k - 1][i][k - 1] + distances[0][tasks[k][0] - 1][tasks[k][1] - 1])
                if k > 0 and i != j and dp[k - 1][i][k - 1] != float('inf'):
                    dp[k][j][k] = min(dp[k][j][k], dp[k - 1][i][k - 2] + distances[tasks[k - 1][0] - 1][tasks[k][0] - 1])

    result = float('inf')
    for i in range(c):
        if dp[-1][i][-1] != float('inf'):
            result = min(result, dp[-1][i][-1] + distances[0][start[0]][start[1]])

    return result if result != float('inf') else "impossible"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    w = int(data[0])
    h = int(data[1])
    c = int(data[2])
    t = int(data[3])
    
    grid = []
    for i in range(h):
        grid.append(list(data[4 + i * w: 4 + (i + 1) * w]))
    
    tasks = []
    for i in range(t):
        x = int(data[4 + h * w + 2 * i])
        y = int(data[5 + h * w + 2 * i])
        tasks.append((x, y))
    
    result = min_steps(w, h, c, t, grid, tasks)
    print(result)

if __name__ == "__main__":
    main()
# Generator time: 105.4451 seconds