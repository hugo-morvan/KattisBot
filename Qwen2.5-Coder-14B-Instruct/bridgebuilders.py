def bfs(grid, start):
    from collections import deque
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start, 0)])
    distances = [[float('inf')] * m for _ in range(n)]
    distances[start[0]][start[1]] = 0
    
    while queue:
        (x, y), dist = queue.popleft()
        
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '.':
                distances[nx][ny] = dist + 1
                queue.append(((nx, ny), dist + 1))
    
    return distances

def solve(grid):
    n = len(grid)
    m = len(grid[0])
    forests = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'T':
                forests.append((i, j))
    
    total_hours = 0
    built_bridges = set()
    
    for forest in forests:
        dists = bfs(grid, forest)
        for i in range(n):
            for j in range(m):
                if (i, j) not in built_bridges and grid[i][j] != '.' and grid[i][j] != 'T':
                    min_dist = float('inf')
                    for fx, fy in forests:
                        if (fx, fy) not in built_bridges:
                            min_dist = min(min_dist, dists[fx][fy])
                    total_hours += min_dist + 1
                    built_bridges.add((i, j))
    
    return total_hours

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for t in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        grid = []
        for _ in range(N):
            grid.append(list(data[index]))
            index += 1
        
        result = solve(grid)
        results.append(result)
    
    for t, result in enumerate(results, start=1):
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()
# Generator time: 75.2515 seconds