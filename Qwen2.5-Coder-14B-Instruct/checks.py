import sys

def parse_move(move):
    if 'x' in move:
        return move.split('x')
    else:
        return [move[:2], move[3:]]

def apply_simple_move(board, start, end):
    x1, y1 = map(int, start)
    x2, y2 = map(int, end)
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = '.'

def apply_jump_move(board, moves):
    for i in range(len(moves) - 1):
        x1, y1 = map(int, moves[i])
        x2, y2 = map(int, moves[i + 1])
        dx = (x2 - x1) // abs(x2 - x1)
        dy = (y2 - y1) // abs(y2 - y1)
        mid_x, mid_y = x1 + dx, y1 + dy
        board[x2][y2] = board[x1][y1]
        board[mid_x][mid_y] = '.'
        board[x1][y1] = '.'

def promote_piece(board, x, y):
    if board[x][y] == 'b' and x == 7:
        board[x][y] = 'B'
    elif board[x][y] == 'w' and x == 0:
        board[x][y] = 'W'

def is_valid_simple_move(board, start, end):
    x1, y1 = map(int, start)
    x2, y2 = map(int, end)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if board[x1][y1] == '.' or board[x2][y2] != '.':
        return False
    if dx != 1 or dy != 1:
        return False
    if board[x1][y1].islower() and (x1 > x2):
        return False
    if board[x1][y1].isupper() and (x1 < x2):
        return False
    return True

def is_valid_jump_move(board, moves):
    for i in range(len(moves) - 1):
        x1, y1 = map(int, moves[i])
        x2, y2 = map(int, moves[i + 1])
        dx = (x2 - x1) // abs(x2 - x1)
        dy = (y2 - y1) // abs(y2 - y1)
        mid_x, mid_y = x1 + dx, y1 + dy
        if board[x1][y1] == '.' or board[x2][y2] != '.' or board[mid_x][mid_y] == '.':
            return False
        if not (board[x1][y1].islower() and board[mid_x][mid_y].isupper()) and not (board[x1][y1].isupper() and board[mid_x][mid_y].islower()):
            return False
    return True

def print_board(board):
    for row in board:
        print(' '.join(row))

def reconstruct_checkers_game(c, moves):
    initial_board = [['-' if (i + j) % 2 == 0 else '.' for j in range(8)] for i in range(8)]
    pieces = ['b', 'w'] if c == 'B' else ['w', 'b']
    
    # Place initial pieces
    for i, row in enumerate(initial_board):
        for j, square in enumerate(row):
            if square == '.':
                initial_board[i][j] = pieces[(i + j) % 2]
    
    board_before = [row[:] for row in initial_board]
    board_after = [row[:] for row in initial_board]
    
    current_player = c
    for move in moves:
        start, *rest = parse_move(move)
        if is_valid_simple_move(board_after, start, rest[0]):
            apply_simple_move(board_after, start, rest[0])
        elif is_valid_jump_move(board_after, [start] + rest):
            apply_jump_move(board_after, [start] + rest)
        else:
            print("Invalid move:", move)
            sys.exit(1)
        
        # Promote pieces
        x2, y2 = map(int, rest[0])
        promote_piece(board_after, x2, y2)
        
        # Switch player
        current_player = 'B' if current_player == 'W' else 'W'
    
    print_board(initial_board)
    print()
    print_board(board_after)

# Read input
c, n = input().split()
moves = [input() for _ in range(int(n))]

# Reconstruct the game
reconstruct_checkers_game(c, moves)
# Generator time: 135.0981 seconds