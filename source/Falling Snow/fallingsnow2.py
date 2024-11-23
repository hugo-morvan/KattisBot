
import sys

# Read input values
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# Function to simulate the falling of snow
def simulate_fall(grid):
    # Iterate over each column
    for col in range(M):
        # Use a temporary list to store the current row of snow
        temp_row = ['.'] * N
        # Iterate over each row from bottom to top
        for row in range(N - 1, -1, -1):
            if grid[row][col] == 'S':
                # If it's snow, move it to the next row
                temp_row[row + 1] = 'S'
                # If the next row is not snow, stop moving
                if row < N - 1 and grid[row + 1][col] != 'S':
                    break
        # Update the original grid with the new row of snow
        grid[row] = ''.join(temp_row)

# Simulate the falling of snow
simulate_fall(grid)

# Output the final configuration of the grid
for row in grid:
    print(row)
