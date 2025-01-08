from collections import deque

def bfs(grid, start, end):
    w, h = len(grid[0]), len(grid)
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        (x, y), steps = queue.popleft()
        
        if (x, y) == end:
            return steps
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    return float('inf')

def find_min_steps(w, h, c, t, grid, tasks):
    start = None
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'K':
                start = (x, y)
                break
    
    total_steps = 0
    current_positions = [start] * c
    
    for task in tasks:
        min_distance = float('inf')
        best_bot = -1
        
        for i, pos in enumerate(current_positions):
            distance = bfs(grid, pos, task)
            if distance < min_distance:
                min_distance = distance
                best_bot = i
        
        total_steps += min_distance
        current_positions[best_bot] = task
    
    return total_steps

def main():
    w, h, c, t = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    tasks = [(int(x) - 1, int(y) - 1) for _ in range(t)]
    
    result = find_min_steps(w, h, c, t, grid, tasks)
    if result == float('inf'):
        print("impossible")
    else:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 14.4641 seconds