from collections import deque

def bfs(start, end, grid, H):
    N, M = len(grid), len(grid[0])
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Queue for BFS
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    
    while queue:
        x, y, time = queue.popleft()
        
        # If we reach the exit, return the time taken
        if (x, y) == end:
            return time
        
        # Check if the current position is already visited
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        # Get the current floor and ceiling heights
        floor = grid[x][y]
        ceiling = grid[N-1-x][M-1-y]
        
        # Check all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds
            if 0 <= nx < N and 0 <= ny < M:
                new_floor = grid[nx][ny]
                new_ceiling = grid[N-1-nx][M-1-ny]
                
                # Check if the new position is accessible
                if new_floor >= floor - 50 and new_ceiling >= ceiling - 50:
                    # Calculate the time to move to the new position
                    if H - time >= 20:
                        new_time = time + 1
                    else:
                        new_time = time + 10
                    
                    # Add the new position to the queue
                    queue.append((nx, ny, new_time))
    
    return float('inf')  # If no path is found

def main():
    T = int(input())
    
    for t in range(1, T + 1):
        H, N, M = map(int, input().split())
        ceiling = [list(map(int, input().split())) for _ in range(N)]
        floor = [list(map(int, input().split())) for _ in range(N)]
        
        # Convert the grid to be easier to access
        grid = [ceiling[i] + [floor[i][::-1]] for i in range(N)]
        
        # Start and end positions
        start = (0, 0)
        end = (N-1, M-1)
        
        # Calculate the time to reach the exit
        time = bfs(start, end, grid, H)
        
        # Print the result
        print(f"Case #{t}: {time:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 39.6160 seconds