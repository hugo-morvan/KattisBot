def count_parking_spaces(R, C, grid):
    # Initialize a 2D list to store the number of cars in each 2x2 block
    cars_in_blocks = [[0] * (C - 1) for _ in range(R - 1)]
    
    # Iterate through the grid to fill the cars_in_blocks list
    for i in range(R - 1):
        for j in range(C - 1):
            if grid[i][j] == 'X' and grid[i + 1][j] == 'X' and grid[i][j + 1] == 'X' and grid[i + 1][j + 1] == 'X':
                cars_in_blocks[i][j] = 4
            elif grid[i][j] == 'X' and grid[i + 1][j] == 'X' and grid[i][j + 1] == 'X':
                cars_in_blocks[i][j] = 3
            elif grid[i][j] == 'X' and grid[i + 1][j] == 'X' or grid[i][j + 1] == 'X' or grid[i + 1][j + 1] == 'X':
                cars_in_blocks[i][j] = 2
            elif grid[i][j] == 'X':
                cars_in_blocks[i][j] = 1
    
    # Count the number of parking spaces for each number of cars
    parking_spaces = [0] * 5
    for row in cars_in_blocks:
        for num_cars in row:
            parking_spaces[num_cars] += 1
    
    # Print the results
    for num_cars in parking_spaces:
        print(num_cars)

# Read input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Call the function with the input values
count_parking_spaces(R, C, grid)