def reconstruct_checkers_board(moves):
    # Initialize the board with '-' for light squares and '.' for empty dark squares
    board = [['-' for _ in range(8)] for _ in range(8)]
    
    # Determine the initial position of the pieces based on the first move
    first_move = moves[0].split('-')
    if first_move[0][0] == 'B':
        board[0][int(first_move[0][1]) - 1] = 'b'
    else:
        board[7][int(first_move[0][1]) - 1] = 'w'
    
    # Apply each move to reconstruct the board
    for move in moves:
        parts = move.split('x')
        current_square = int(parts[0][0]) - 1
        target_squares = [int(part[1:]) - 1 for part in parts]
        
        if len(target_squares) > 1:
            # Handle jump move
            for i in range(len(target_squares) - 1):
                board[current_square][i] = '.'
                board[target_squares[i]][i] = '.'
                board[target_squares[i + 1]][i + 1] = 'B' if parts[0][0] == 'B' else 'W'
                current_square = target_squares[i + 1]
        else:
            # Handle simple move
            board[current_square][0] = '.'
            board[target_squares[0]][0] = 'B' if parts[0][0] == 'B' else 'W'
    
    # Convert the board to the required output format
    def board_to_string(board):
        result = []
        for row in board:
            result.append(''.join(row))
        return ' '.join(result)
    
    # Print the initial and final boards
    print(board_to_string(board))

# Read input
c, n = input().split()
moves = [input() for _ in range(int(n))]

# Reconstruct the board
reconstruct_checkers_board(moves)
# Generator time: 20.9622 seconds