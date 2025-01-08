def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if 'num' is not in the current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for row in board:
        print("".join(str(num) for num in row))
    print()


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    while index < len(data):
        if not data[index]:
            index += 1
            continue

        board = []
        for _ in range(9):
            row = list(map(int, data[index]))
            board.append(row)
            index += 1

        # Create a copy of the original board to check solvability
        original_board = [row[:] for row in board]

        if not solve_sudoku(board):
            print("Find another job")
        else:
            # Check for uniqueness
            solve_sudoku(original_board)  # Reset the board to its initial state
            if not solve_sudoku(board):  # Try solving again
                print("Non-unique")
            else:
                print_board(board)

        index += 1


if __name__ == "__main__":
    main()
# Generator time: 68.5478 seconds