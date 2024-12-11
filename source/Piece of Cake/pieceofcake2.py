# Read input values
n, h, v = map(int, input().split())

# Calculate the volume of each piece
piece1 = h * v * 4  # Top-left piece
piece2 = (n - h) * v * 4  # Bottom-left piece
piece3 = h * (n - v) * 4  # Top-right piece
piece4 = (n - h) * (n - v) * 4  # Bottom-right piece

# Determine the maximum volume
max_volume = max(piece1, piece2, piece3, piece4)

# Print the result
print(max_volume)