import sys
from collections import deque

def min_moves_to_goal(maze):
    C = len(maze[0])
    R = len(maze)
    
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def is_valid(x, y):
        return 0 <= x < R and 0 <= y < C and maze[x][y] != '#'
    
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y, 0)])
        visited = [[False for _ in range(C)] for _ in range(R)]
        visited[start_x][start_y] = True
        
        while queue:
            x, y, moves = queue.popleft()
            
            if maze[x][y] == 'M':
                return moves
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if is_valid(nx, ny):
                    new_moves = moves
                    while is_valid(nx + dx, ny + dy) and maze[nx + dx][ny + dy] == '_':
                        nx += dx
                        ny += dy
                        new_moves += 1
                    
                    if not visited[nx][ny]:
                        queue.append((nx, ny, new_moves))
                        visited[nx][ny] = True
        
        return -1
    
    result = [[-1 for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if is_valid(i, j):
                result[i][j] = bfs(i, j)
    
    return result

# Read input
C, R = map(int, input().split())
maze = [input() for _ in range(R)]

# Calculate and print the result
result = min_moves_to_goal(maze)
for row in result:
    print(' '.join(map(str, row)))
# Generator time: 12.9435 seconds