def count_safe_squares(X, Y, N, queens):
    # Initialize a set to store the positions of the existing queens
    queen_positions = set()
    
    # Add the positions of the existing queens to the set
    for x, y in queens:
        queen_positions.add((x - 1, y - 1))
    
    # Initialize a counter for safe squares
    safe_count = 0
    
    # Iterate over each possible square on the board
    for x in range(X):
        for y in range(Y):
            # Check if the current square is not occupied and not on the same row, column, or diagonal
            if (x, y) not in queen_positions:
                safe = True
                for qx, qy in queen_positions:
                    if x == qx or y == qy or abs(x - qx) == abs(y - qy):
                        safe = False
                        break
                if safe:
                    safe_count += 1
    
    return safe_count

# Read input
tasks = []
while True:
    line = input().strip()
    if line == '0 0 0':
        break
    X, Y, N = map(int, line.split())
    queens = [tuple(map(int, input().split())) for _ in range(N)]
    tasks.append((X, Y, N, queens))

# Process each task
for X, Y, N, queens in tasks:
    result = count_safe_squares(X, Y, N, queens)
    print(result)
# Generator time: 21.9105 seconds