def max_moves(A, B, C):
    # Calculate the minimum distance between any two kangaroos
    min_distance = min(abs(B - A), abs(C - B), abs(C - A))
    
    # Since each move reduces the minimum distance by at least 1, the maximum number of moves is
    # the minimum distance divided by 2 (rounded down)
    return min_distance // 2

# Read input
A, B, C = map(int, input().split())

# Calculate and print the maximum number of moves
print(max_moves(A, B, C))