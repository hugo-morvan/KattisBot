def calculate_moves(maze):
    R, C = len(maze), len(maze[0])
    goal = None

    # Find the goal position
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'M':
                goal = (r, c)
                break
        if goal:
            break

    if not goal:
        return [[-1] * C for _ in range(R)]

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the distance matrix with infinity
    distance = [[float('inf')] * C for _ in range(R)]
    distance[goal[0]][goal[1]] = 0

    queue = [(goal[0], goal[1])]

    while queue:
        current_r, current_c = queue.pop(0)

        for dr, dc in directions:
            new_r, new_c = current_r + dr, current_c + dc

            # Check if the new position is within bounds
            if 0 <= new_r < R and 0 <= new_c < C:
                # Check if the new position is an obstacle
                if maze[new_r][new_c] == '#':
                    continue
                # If the new position is ice, add it to the queue
                elif maze[new_r][new_c] == '_':
                    if distance[current_r][current_c] + 1 < distance[new_r][new_c]:
                        distance[new_r][new_c] = distance[current_r][current_c] + 1
                        queue.append((new_r, new_c))
                # If the new position is gravel, update the distance
                else:
                    if distance[current_r][current_c] + 1 < distance[new_r][new_c]:
                        distance[new_r][new_c] = distance[current_r][current_c] + 1

    # Convert distances to the required output format
    result = []
    for r in range(R):
        row = []
        for c in range(C):
            if distance[r][c] == float('inf'):
                row.append(-1)
            else:
                row.append(distance[r][c])
        result.append(row)

    return result

# Read input
C, R = map(int, input().split())
maze = [input().strip() for _ in range(R)]

# Calculate and print the results
result = calculate_moves(maze)
for row in result:
    print(' '.join(map(str, row)))
# Generator time: 25.2273 seconds