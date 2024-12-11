import sys

# Read input
M = int(input())
temperatures = list(map(int, input().split()))

# Calculate the mean temperature
mean_temperature = sum(temperatures) // M

# Print the result
print(mean_temperature)