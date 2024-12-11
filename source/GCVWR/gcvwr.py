# Read input values
G, T, N = map(int, input().split())
weights = list(map(int, input().split()))

# Calculate remaining towing capacity
remaining_capacity = G - T

# Calculate the maximum allowed weight for the trailer
max_trailer_weight = int(0.9 * remaining_capacity)

# Initialize variables to track the maximum trailer weight
max_weight = 0

# Iterate through each item to find the maximum trailer weight
for weight in weights:
    if max_trailer_weight - weight >= 0:
        max_weight = max(max_weight, weight)

print(max_weight)