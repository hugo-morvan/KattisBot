def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_scatter(puzzle):
    desired_layout = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', '.']
    ]
    
    scatter = 0
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] != '.':
                x, y = i, j
                x_desired, y_desired = desired_layout.index([puzzle[i][j]]), desired_layout[x][y]
                scatter += manhattan_distance(x, y, x_desired, y_desired)
    
    return scatter

# Read input
puzzle = []
for _ in range(4):
    puzzle.append(input().strip())

# Calculate and print the scatter
print(calculate_scatter(puzzle))