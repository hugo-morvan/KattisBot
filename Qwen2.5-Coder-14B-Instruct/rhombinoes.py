def max_rhombinoes(W, H, K, dead_triangles):
    # Create a 2D list to represent the board
    board = [[1] * W for _ in range(H)]
    
    # Mark the dead triangles
    for x, y in dead_triangles:
        board[y][x] = 0
    
    # Function to check if a rhombino can be placed at (x, y)
    def can_place_rhombino(x, y):
        # Check right and top adjacency
        if x + 1 < W and y + 1 < H:
            return board[y][x] == 1 and board[y+1][x] == 1 and board[y][x+1] == 1 and board[y+1][x+1] == 1
        return False
    
    # Function to place a rhombino at (x, y)
    def place_rhombino(x, y):
        board[y][x] = 0
        board[y+1][x] = 0
        board[y][x+1] = 0
        board[y+1][x+1] = 0
    
    # Function to remove a rhombino at (x, y)
    def remove_rhombino(x, y):
        board[y][x] = 1
        board[y+1][x] = 1
        board[y][x+1] = 1
        board[y+1][x+1] = 1
    
    # Try to place rhombinoes
    max_rhombino_count = 0
    for y in range(H):
        for x in range(W):
            if can_place_rhombino(x, y):
                place_rhombino(x, y)
                max_rhombino_count += 1
    
    return max_rhombino_count

# Read input
W, H, K = map(int, input().split())
dead_triangles = [tuple(map(int, input().split())) for _ in range(K)]

# Calculate and print the result
print(max_rhombinoes(W, H, K, dead_triangles))
# Generator time: 60.4796 seconds