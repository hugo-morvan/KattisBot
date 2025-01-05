import sys
from collections import deque

def find_num_carriages():
    n = int(input())
    s = int(input())
    
    # Initialize the queue with the starting carriage
    queue = deque([0])
    visited = set([0])
    
    # Perform BFS
    while queue:
        current = queue.popleft()
        
        # Check if we have found all carriages
        if len(visited) == n:
            break
        
        # Get the state of the current carriage
        current_state = s
        
        # Explore the left and right carriages
        left = (current - 1) % n
        right = (current + 1) % n
        
        # Toggle the current carriage
        if current_state == 0:
            current_state = 1
        else:
            current_state = 0
        
        # Add the left and right carriages to the queue if they haven't been visited
        if left not in visited:
            queue.append(left)
            visited.add(left)
            print("left")
            s = int(input())
        
        if right not in visited:
            queue.append(right)
            visited.add(right)
            print("right")
            s = int(input())
        
        # Toggle the current carriage again
        if current_state == 0:
            current_state = 1
        else:
            current_state = 0
        
        # Add the current carriage back to the queue if it hasn't been visited
        if current not in visited:
            queue.append(current)
            visited.add(current)
            print("flip")
            s = int(input())
    
    # Print the number of carriages
    print(f"! {len(visited)}")

find_num_carriages()
# Generator time: 17.0589 seconds