def max_rhombinoes(W, H, K, dead_triangles):
    # Initialize the board with all live triangles
    board = [[True] * H for _ in range(W)]
    
    # Mark the dead triangles
    for x, y in dead_triangles:
        board[x][y] = False
    
    # Count the number of live triangles
    live_triangles_count = sum(sum(row) for row in board)
    
    # Calculate the maximum number of rhombinoes
    max_rhombinoes = live_triangles_count // 2
    
    return max_rhombinoes

# Read input
W, H, K = map(int, input().split())
dead_triangles = [tuple(map(int, input().split())) for _ in range(K)]

# Compute and print the result
print(max_rhombinoes(W, H, K, dead_triangles))
# Generator time: 21.8566 seconds