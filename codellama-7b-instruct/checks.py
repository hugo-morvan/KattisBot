import itertools as it

def solve(moves):
    board = [['-'] * 32 for _ in range(8)]
    black = True
    moves = iter(moves)
    while (next(moves, None)): # while there are still moves to do
        if black: # Black's turn.
            move_type, src, dst = next(moves).split('-')
            if move_type == 'B':
                board[int(dst) // 8][int(dst) % 8] = 'B'
            elif move_type == 'W':
                board[int(src) // 8][int(src) % 8] = 'w'
        else: # White's turn.
            move_type, src, dst = next(moves).split('-')
            if move_type == 'B':
                board[int(src) // 8][int(src) % 8] = 'b'
            elif move_type == 'W':
                board[int(dst) // 8][int(dst) % 8] = 'w'
        black = not black
    return board
# Generator time: 16.5358 seconds