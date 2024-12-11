# Read the grades for each contestant
grades = [list(map(int, input().split())) for _ in range(5)]

# Calculate the total points for each contestant
points = [sum(grades[i]) for i in range(5)]

# Find the index of the contestant with the maximum points
winner_index = points.index(max(points))

# Print the winner's number and their points
print(winner_index + 1, max(points))