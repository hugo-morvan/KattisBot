# Read input values
A, B = map(int, input().split())
N = int(input())
floors_to_stop = list(map(int, input().split()))

# Calculate the total time the elevator will take to move from A to B
total_move_time = abs(B - A) * 4

# Calculate the time spent inside the elevator
time_inside_elevator = 0

# Iterate through the floors that the elevator will stop at
for floor in floors_to_stop:
    # If the floor is between A and B, add the time spent on that floor
    if A <= floor <= B:
        time_inside_elevator += 10

# Print the total time Loke has to suffer inside the elevator
print(total_move_time + time_inside_elevator)