def count_safe_squares(X, Y, N, queens):
    # Initialize sets to keep track of rows, columns, and diagonals
    rows = set()
    cols = set()
    diag1 = set()  # y - x
    diag2 = set()  # y + x

    # Populate the sets with occupied positions
    for x, y in queens:
        rows.add(x)
        cols.add(y)
        diag1.add(y - x)
        diag2.add(y + x)

    # Count the number of safe squares
    safe_squares = 0
    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            if (x not in rows and y not in cols and 
                y - x not in diag1 and y + x not in diag2):
                safe_squares += 1

    return safe_squares

def main():
    while True:
        X, Y, N = map(int, input().split())
        if X == 0 and Y == 0 and N == 0:
            break
        queens = [tuple(map(int, input().split())) for _ in range(N)]
        result = count_safe_squares(X, Y, N, queens)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 37.6157 seconds