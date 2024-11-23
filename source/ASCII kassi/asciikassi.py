def draw_square(N):
    if N == 0:
        print("++")
        return
    
    # Top border
    print("+", end="")
    for _ in range(2 * N - 1):
        print("-", end="")
    print("+")
    
    # Middle rows
    for _ in range(N - 2):
        print("|", end="")
        for _ in range(2 * N - 2):
            print(" ", end="")
        print("|")
    
    # Bottom border
    print("+", end="")
    for _ in range(2 * N - 1):
        print("-", end="")
    print("+")

# Read input
N = int(input())

# Draw the square
draw_square(N)