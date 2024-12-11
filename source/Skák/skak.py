def min_moves_to_capture_rook(x_r, y_r, x_p, y_p):
    # Calculate the horizontal and vertical distances
    horizontal_distance = abs(x_r - x_p)
    vertical_distance = abs(y_r - y_p)
    
    # The minimum number of moves is the maximum of the two distances
    min_moves = max(horizontal_distance, vertical_distance)
    
    return min_moves

# Read input
x_r, y_r = map(int, input().split())
x_p, y_p = map(int, input().split())

# Calculate and print the minimum number of moves
print(min_moves_to_capture_rook(x_r, y_r, x_p, y_p))