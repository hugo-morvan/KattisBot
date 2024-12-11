def simulate_snowfall(N, M, grid):
    # Create a new grid to store the final state of the snow
    final_grid = [['.' for _ in range(M)] for _ in range(N)]
    
    # Iterate over each row in the grid
    for i in range(N):
        # Iterate over each column in the row
        for j in range(M):
            # If the current cell contains snow ('S')
            if grid[i][j] == 'S':
                # Find the lowest possible position for the snow
                k = i
                while k < N and grid[k][j] != 'S':
                    k += 1
                
                # Place the snow in the final grid at the lowest position
                final_grid[k-1][j] = 'S'
    
    # Join the rows of the final grid into a single string
    return '\n'.join(''.join(row) for row in final_grid)

# Read input
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Simulate the snowfall and print the result
result = simulate_snowfall(N, M, grid)
print(result)