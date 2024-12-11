# Read the input time
H, M = map(int, input().split())

# Calculate the new time after subtracting 45 minutes
new_M = M - 45

# If the new minutes are negative, adjust hours and minutes
if new_M < 0:
    H -= 1
    new_M += 60

# Print the new time in 24-hour notation
print(f"{H:02d} {new_M:02d}")