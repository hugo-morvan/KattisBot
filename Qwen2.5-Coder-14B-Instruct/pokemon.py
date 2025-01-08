from collections import deque

def get_moves_to_goal(C, R, maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    goal = None
    
    # Find the goal position
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'M':
                goal = (r, c)
                break
        if goal:
            break

    # Initialize the distance matrix with -1 and set the goal to 0 moves
    distances = [[-1 for _ in range(C)] for _ in range(R)]
    distances[goal[0]][goal[1]] = 0
    
    # BFS queue
    queue = deque([goal])
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            moves = 1
            
            # Glide on ice
            while 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#':
                if distances[nr][nc] == -1 or distances[nr][nc] > distances[r][c] + moves:
                    distances[nr][nc] = distances[r][c] + moves
                    queue.append((nr, nc))
                
                if maze[nr][nc] == '.':
                    break
                
                nr += dr
                nc += dc
                moves += 1
    
    return distances

# Read input
C, R = map(int, input().split())
maze = [input().strip() for _ in range(R)]

# Get the result
result = get_moves_to_goal(C, R, maze)

# Print the result
for row in result:
    print(' '.join(map(str, row)))
# Generator time: 50.9562 seconds