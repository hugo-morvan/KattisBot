import math

# Read input values
h, v = map(int, input().split())

# Convert angle from degrees to radians
angle_radians = v * (math.pi / 180)

# Calculate the length of the ladder
ladder_length = h / math.sin(angle_radians)

# Round up to the nearest integer
ladder_length_rounded = math.ceil(ladder_length)

# Print the result
print(ladder_length_rounded)