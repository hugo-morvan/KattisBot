def check_winner(board):
    # Check rows
    for row in board:
        if row == 'XXX':
            return 'Jebb'
        elif row == 'OOO':
            return 'Neibb'

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return 'Jebb'
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return 'Neibb'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X' or \
       board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'Jebb'
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or \
       board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'Neibb'

    # No winner
    return 'Neibb'

# Read input
board = [input().strip() for _ in range(3)]

# Check and print the result
result = check_winner(board)
print(result)