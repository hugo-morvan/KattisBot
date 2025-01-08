def find_safe_squares():
    while True:
        X, Y, N = map(int, input().split())
        if X == 0 and Y == 0 and N == 0:
            break
        
        # Initialize a set to keep track of occupied positions
        occupied = set()
        
        for _ in range(N):
            x, y = map(int, input().split())
            occupied.add((x, y))
        
        # Count the number of safe squares
        safe_squares = 0
        for i in range(1, X + 1):
            for j in range(1, Y + 1):
                if (i, j) not in occupied:
                    # Check if the square is on the same row, column, or diagonal
                    if all((i != x and j != y) and abs(i - x) != abs(j - y) for x, y in occupied):
                        safe_squares += 1
        
        print(safe_squares)

find_safe_squares()
# Generator time: 7.5317 seconds