# Read input values
N = int(input())
rooms = []

for _ in range(N):
    g, b = map(int, input().split())
    rooms.append((g, b))

# Initialize current Goombas
current_goombas = 0

# Process each room
for i in range(N):
    g, b = rooms[i]
    current_goombas += g - b
    
    # Check if Mario can escape
    if current_goombas <= 0:
        print("impossible")
        break

else:
    print("possible")