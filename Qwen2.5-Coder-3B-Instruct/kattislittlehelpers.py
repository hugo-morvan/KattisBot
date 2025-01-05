def min_steps_to_visit_locations(w, h, c, t, grid, tasks):
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Find Kattis' HQ position
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'K':
                KattisHQ_x, KattisHQ_y = i, j
                break
    
    # Initialize DP table with infinity
    dp = [[float('inf')] * w for _ in range(h)]
    dp[KattisHQ_x][KattisHQ_y] = 0
    
    # Priority queue to store cells to visit, initially only Kattis' HQ
    pq = [(0, KattisHQ_x, KattisHQ_y)]
    
    while pq:
        current_steps, x, y = heapq.heappop(pq)
        
        # If we've visited all tasks, check if we can return to HQ
        if len(tasks) == 0:
            return current_steps
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '#' and dp[nx][ny] > current_steps + 1:
                dp[nx][ny] = current_steps + 1
                heapq.heappush(pq, (dp[nx][ny], nx, ny))
    
    # If we couldn't visit all tasks, return "impossible"
    return "impossible"

# Read input
import sys
input = sys.stdin.read
data = input().split()

w, h, c, t = map(int, data[:4])
grid = [list(data[4:4+w])] + [list(data[4+w+i*2]) for i in range(t)]
tasks = [(int(data[4+w+t+i*2]), int(data[4+w+t+i*2+1])) for i in range(t)]

# Find the minimum steps
result = min_steps_to_visit_locations(w, h, c, t, grid, tasks)
print(result)
# Generator time: 41.0774 seconds