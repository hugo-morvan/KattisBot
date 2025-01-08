import sys

def flush():
    sys.stdout.flush()

# Read the initial state of the light switch
initial_state = int(input().strip())

# Initialize variables
visited = set()
current_carriage = 0
steps = 0
max_steps = 3 * 5000 + 500

while steps < max_steps:
    # If we have visited this carriage before, we found a cycle
    if current_carriage in visited:
        n = len(visited)
        print(f"! {n}")
        flush()
        break
    
    # Mark the current carriage as visited
    visited.add(current_carriage)
    
    # Move to an adjacent carriage (try both directions)
    if steps % 2 == 0:
        move = "right"
    else:
        move = "left"
    
    print(f"? {move}")
    flush()
    
    # Read the new state of the light switch
    current_state = int(input().strip())
    
    # Move to the next carriage based on the direction
    if move == "right":
        current_carriage += 1
    else:
        current_carriage -= 1
    
    steps += 1

# If we reach here without finding a cycle, something went wrong
if steps >= max_steps:
    print("Error: Exceeded maximum number of steps")
    flush()
# Generator time: 38.3825 seconds