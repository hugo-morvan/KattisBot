# Read input values
W = int(input())  # Width of the cake
N = int(input())  # Number of shattered pieces

# Initialize the total length of the cake
total_length = 0

# Iterate over each shattered piece
for _ in range(N):
    w, l = map(int, input().split())  # Read width and length of the piece
    total_length += l  # Add the length of the current piece to the total

# Output the total length of the cake
print(total_length)