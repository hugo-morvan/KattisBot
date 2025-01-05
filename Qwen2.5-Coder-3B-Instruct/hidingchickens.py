import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Read input
roost_x, roost_y = map(float, input().split())
N = int(input())

# List to store the coordinates of hiding spots
hiding_spots = []
for _ in range(N):
    x, y = map(float, input().split())
    hiding_spots.append((x, y))

# Sort hiding spots based on their distance from the roost
hiding_spots.sort(key=lambda spot: euclidean_distance(roost_x, roost_y, *spot))

# Initialize variables
total_distance = 0
i = 0

# Pair the closest chickens with the closest hiding spots
while i < len(hiding_spots):
    # Move to the closest hiding spot
    total_distance += euclidean_distance(roost_x, roost_y, *hiding_spots[i])
    i += 1
    
    # If there are still chickens left, move back to the roost
    if i < len(hiding_spots):
        total_distance += euclidean_distance(*hiding_spots[i], roost_x, roost_y)
        i += 1

# Print the result
print(total_distance)
# Generator time: 26.3218 seconds