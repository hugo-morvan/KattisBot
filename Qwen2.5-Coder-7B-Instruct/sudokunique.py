def solve_sudoku(board):
    def find_empty_location(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(board, num, pos):
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(board):
        find = find_empty_location(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if is_valid(board, i, (row, col)):
                board[row][col] = i

                if solve(board):
                    return True

                board[row][col] = 0

        return False

    if solve(board):
        return board
    else:
        return None

def main():
    boards = []
    while True:
        try:
            board = [list(map(int, input().split())) for _ in range(9)]
            boards.append(board)
        except EOFError:
            break

    results = []
    for board in boards:
        solved_board = solve_sudoku(board)
        if solved_board is None:
            results.append("Non-unique")
        else:
            result = [[str(num) for num in row] for row in solved_board]
            if solve_sudoku(solved_board):
                results.append('\n'.join(' '.join(row) for row in result))
            else:
                results.append("Find another job")

    for result in results:
        print(result)
        if result != "Non-unique" and result != "Find another job":
            print()

main()
# Generator time: 14.6761 seconds