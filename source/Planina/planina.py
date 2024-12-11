def calculate_points(N):
    # Base case: 4 points at the start
    points = 4
    
    for i in range(1, N + 1):
        # Each iteration adds 4 new points per square
        points += 4 ** (i - 1) * 4
    
    return points

# Read input
N = int(input())

# Calculate and print the number of points needed
print(calculate_points(N))