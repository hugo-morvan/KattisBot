# Read the number of photographs
n = int(input())

# Initialize variables to store the maximum speed and the previous time and distance
max_speed = 0
prev_time = 0
prev_distance = 0

# Iterate over each photograph
for _ in range(n):
    # Read the time and distance of the current photograph
    time, distance = map(int, input().split())
    
    # Calculate the speed between the current and previous photograph
    if time > prev_time:
        speed = (distance - prev_distance) / (time - prev_time)
        max_speed = max(max_speed, speed)
    
    # Update the previous time and distance
    prev_time = time
    prev_distance = distance

# Output the maximum speed
print(int(max_speed))