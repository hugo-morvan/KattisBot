def parse_move(move):
    if 'x' in move:
        parts = move.split('x')
        start = int(parts[0]) - 1
        jumps = [int(p) - 1 for p in parts[1:]]
        return start, jumps
    else:
        start, end = map(int, move.split('-'))
        return start - 1, end - 1

def apply_move(board, start, jump):
    if board[start] == 'b':
        new_piece = 'B' if jump % 2 == 0 else 'b'
    elif board[start] == 'w':
        new_piece = 'W' if jump % 2 == 0 else 'w'
    else:
        return False
    
    for j in range(jump):
        if not (0 <= start + 8 * (j // 4) + [1, -1, 8, -8][j % 4] < len(board)):
            return False
        board[start + 8 * (j // 4) + [1, -1, 8, -8][j % 4]] = '.'
    board[start] = new_piece
    return True

def apply_moves(moves):
    board_before = ['-'] * 32
    board_after = ['.'] * 32
    
    for move in moves:
        start, jumps = parse_move(move)
        if 'x' in move:
            for j in jumps:
                if not apply_move(board_before.copy(), start, j + 1):
                    return None, None
        else:
            if not apply_move(board_before.copy(), start, 2):
                return None, None
    
    return board_before, board_after

def print_board(board):
    result = []
    for i in range(8):
        row = ''.join(board[i*4:(i+1)*4])
        result.append(' '.join(row))
    return '\n'.join(result)

def main():
    input_line = input().strip()
    c, n = input_line[0], int(input_line[2:])
    
    moves = [input().strip() for _ in range(n)]
    
    board_before, board_after = apply_moves(moves)
    
    if board_before is None or board_after is None:
        print("No valid solution")
    else:
        print(print_board(board_before), print_board(board_after), sep=' ')

if __name__ == "__main__":
    main()
# Generator time: 15.2063 seconds