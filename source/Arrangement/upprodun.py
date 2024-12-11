# Read input values
N = int(input())
M = int(input())

# Calculate the number of teams per room
teams_per_room = M // N
remainder = M % N

# Initialize the list of rooms with empty lists
rooms = [[] for _ in range(N)]

# Distribute teams into rooms
for i in range(M):
    # Determine the room number based on the remainder
    room_number = i % N
    # Add the team to the corresponding room
    rooms[room_number].append('*')

# Print the output for each room
for room in rooms:
    print(''.join(room))