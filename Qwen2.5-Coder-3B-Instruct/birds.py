# Read input values
l, d, n = map(int, input().split())
birds = sorted(map(int, input().split()))

# Initialize variables
max_birds = 0
current_pos = 0

# Iterate through the list of birds
for bird in birds:
    # Calculate the position where the next bird can sit
    next_pos = bird + d
    # Check if the next position is within the wire and not occupied
    if next_pos <= l and current_pos < next_pos:
        # Add the number of birds that can fit between the current and next bird
        max_birds += (next_pos - current_pos - 1) // d
        current_pos = next_pos

# Print the result
print(max_birds)
# Generator time: 6.9607 seconds