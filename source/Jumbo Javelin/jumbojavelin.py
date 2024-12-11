# Read the number of steel rods
N = int(input())

# Initialize the total length of the rods
total_length = 0

# Read the lengths of each rod
for _ in range(N):
    length = int(input())
    total_length += length

# Calculate the length of the jumbo javelin
jumbo_length = total_length - (N - 1)

# Print the length of the jumbo javelin
print(jumbo_length)