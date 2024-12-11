def find_message(grid):
    N, M = len(grid), len(grid[0])
    
    # Directions: right and down
    directions = [(0, 1), (1, 0)]
    
    def backtrack(x, y, path):
        # Base case: if we reach the bottom-right corner
        if x == N - 1 and y == M - 1:
            return ''.join(path)
        
        # Try moving right
        if y + 1 < M and grid[x][y + 1] != '.':
            result = backtrack(x, y + 1, path + [grid[x][y + 1]])
            if result:
                return result
        
        # Try moving down
        if x + 1 < N and grid[x + 1][y] != '.':
            result = backtrack(x + 1, y, path + [grid[x + 1][y]])
            if result:
                return result
        
        return None
    
    # Start the backtracking from the top-left corner
    return backtrack(0, 0, [grid[0][0]])

# Read input
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Find and print the message
message = find_message(grid)
print(message)