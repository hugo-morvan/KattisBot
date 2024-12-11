# Read input values
a = int(input())
b = int(input())
c = int(input())

# Calculate the latest possible starting time
latest_start_time = max(c - (a + b), 720)

# Output the result
print(latest_start_time)