from collections import defaultdict
import math

n, m = map(int, input().split())

# Create a dictionary to store the coordinates of each citizen
citizens = {}
for i in range(n):
    x, y = map(int, input().split())
    citizens[i] = [x, y]

# Create a dictionary to store the train lines and their respective capacities
train_lines = defaultdict(list)
for j in range(m):
    x, y, c = map(int, input().split())
    train_lines[(x,y)] = c

# Initialize the distances between each citizen and the central hub to infinity
distances = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        # Calculate the angular distance between the citizens
        dist = math.acos(((citizens[i][0] - citizens[j][0]) ** 2 + (citizens[i][1] - citizens[j][1]) ** 2) ** 0.5)
        # Set the angular distance to its inverse if the train lines overlap
        try:
            dist = min(dist, math.acos(((citizens[i][0] - train_lines[(x,y)][0]) ** 2 + (citizens[i][1] - train_lines[(x,y)][1]) ** 2) ** 0.5))
            dist = min(dist, math.acos(((train_lines[(x,y)][0] - citizens[j][0]) ** 2 + (train_lines[(x,y)][1] - citizens[j][1]) ** 2) ** 0.5))
        except:
            pass
        distances[i][j] = dist
        distances[j][i] = dist

# Initialize the maximum size of the subset to be zero and the indices of the citizens in the subset to be empty
subset_size = 0
indices = []

# Find the maximum size of the subset using dynamic programming
for k in range(n):
    for i in range(k+1):
        # Add each citizen to the subset at most once and only if they are closest to the central hub
        for j in range(i+1, n):
            dist = distances[j][k]
            if dist < distances[i][j]:
                dist = distances[i][j]
            try:
                dist = min(dist, (math.pi - distances[i][j]) + math.pi - distances[j][k])
            except:
                pass
            if dist <= train_lines[(x,y)]:
                indices.append([i, j])
                subset_size += 1
                break
print(subset_size)
for pair in indices:
    print(pair[0], pair[1])
# Generator time: 17.0301 seconds