def is_valid(board):
    # Check rows, columns, and 3x3 subgrids for duplicates
    for i in range(9):
        if not is_unique(board[i]):
            return False
        if not is_unique([board[j][i] for j in range(9)]):
            return False
        if not is_unique([board[i//3*3+j//3][i%3*3+j%3] for j in range(9)]):
            return False
    return True

def is_unique(lst):
    return len(lst) == len(set(lst))

def solve_sudoku(board):
    def backtrack(row, col):
        if row == 9:
            return True
        if col == 9:
            return backtrack(row + 1, 0)
        if board[row][col] != 0:
            return backtrack(row, col + 1)
        
        for num in range(1, 10):
            board[row][col] = num
            if is_valid(board):
                if backtrack(row, col + 1):
                    return True
            board[row][col] = 0
        return False
    
    if not is_valid(board):
        return "Find another job"
    
    if not backtrack(0, 0):
        return "Non-unique"
    
    return board

def main():
    while True:
        board = []
        try:
            while True:
                line = input().strip()
                if not line:
                    break
                board.append(list(map(int, line)))
            if not board:
                break
            solution = solve_sudoku(board)
            print('\n'.join(' '.join(map(str, row)) for row in solution))
            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()
# Generator time: 19.4466 seconds