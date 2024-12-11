def count_islands(r, c, grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= r or y >= c or grid[x][y] != 'L':
            return
        grid[x][y] = 'X'  # Mark as visited
        dfs(x + 1, y)  # Down
        dfs(x - 1, y)  # Up
        dfs(x, y + 1)  # Right
        dfs(x, y - 1)  # Left

    island_count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'L':
                dfs(i, j)
                island_count += 1
    return island_count

# Read input
r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]

# Calculate and print the minimum number of islands
print(count_islands(r, c, grid))