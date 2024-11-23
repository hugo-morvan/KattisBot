# Read input values
n, m, k = map(int, input().split())
mine_locations = [tuple(map(int, input().split())) for _ in range(k)]

# Initialize the board with empty cells
board = [['.' for _ in range(m)] for _ in range(n)]

# Place mines on the board
for y, x in mine_locations:
    board[y-1][x-1] = '*'

# Function to calculate the number of adjacent mines for each cell
def count_adjacent_mines(y, x):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if 0 <= y + dy < n and 0 <= x + dx < m and board[y + dy][x + dx] == '*':
                count += 1
    return count

# Fill in the numbers on the board
for y in range(n):
    for x in range(m):
        if board[y][x] == '.':
            board[y][x] = str(count_adjacent_mines(y, x))

# Print the board
for row in board:
    print(''.join(row))