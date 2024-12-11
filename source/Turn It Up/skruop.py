# Read the number of requests
n = int(input())

# Initialize the volume control
volume = 7

# Process each request
for _ in range(n):
    request = input()
    if request == "Skru op!":
        if volume < 10:
            volume += 1
    elif request == "Skru ned!":
        if volume > 0:
            volume -= 1

# Print the final volume control position
print(volume)