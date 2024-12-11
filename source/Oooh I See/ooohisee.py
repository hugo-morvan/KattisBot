def find_treasure(rows, cols, grid):
    treasure_locations = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                # Check if all surrounding cells are 'O'
                if (i > 0 and grid[i-1][j] == 'O') and \
                   (i < rows-1 and grid[i+1][j] == 'O') and \
                   (j > 0 and grid[i][j-1] == 'O') and \
                   (j < cols-1 and grid[i][j+1] == 'O') and \
                   (i > 0 and j > 0 and grid[i-1][j-1] == 'O') and \
                   (i > 0 and j < cols-1 and grid[i-1][j+1] == 'O') and \
                   (i < rows-1 and j > 0 and grid[i+1][j-1] == 'O') and \
                   (i < rows-1 and j < cols-1 and grid[i+1][j+1] == 'O'):
                    treasure_locations.append((i+1, j+1))
    
    if len(treasure_locations) == 0:
        print("Oh no!")
    elif len(treasure_locations) > 1:
        print("Oh no! " + str(len(treasure_locations)) + " locations")
    else:
        print(treasure_locations[0][0], treasure_locations[0][1])

# Read input
rows, cols = map(int, input().split())
grid = [input() for _ in range(rows)]

# Find and print the treasure location
find_treasure(rows, cols, grid)