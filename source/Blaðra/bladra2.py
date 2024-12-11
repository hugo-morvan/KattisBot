# Read input values
v, a, t = map(int, input().split())

# Calculate the distance traveled by the balloon
d = v * t + 0.5 * a * t**2

# Print the result
print(d)