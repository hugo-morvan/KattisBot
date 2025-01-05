import numpy as np

def can_reach_bob(R, l, w, A, B):
    # Convert angles to radians
    A_rad = np.radians(A)
    B_rad = np.radians(B)
    
    # Define the positions of the doors
    x1 = w / 2 - l / 2
    x2 = w / 2 + l / 2
    
    # Define the initial and final positions of Alex and Bob
    start = np.array([0, 0])
    end = np.array([w, w / 2])
    
    # Define the directions of the doors
    door1_dir = np.array([1, 0])
    door2_dir = np.array([-1, 0])
    
    # Define the direction of Alex's movement
    alex_dir = np.array([np.cos(A_rad), np.sin(A_rad)])
    
    # Define the direction of Bob's movement
    bob_dir = np.array([np.cos(B_rad), np.sin(B_rad)])
    
    # Check if Alex can reach Bob by avoiding the doors
    def check_path(r):
        # Check if the path intersects with the doors
        def is_intersecting(path, door_start, door_dir):
            # Calculate the intersection point
            t1 = (door_start[0] - path[0]) / door_dir[0]
            t2 = (path[-1][0] - door_start[0]) / door_dir[0]
            if t1 < 0 or t2 > 1:
                return False
            intersection = door_start + door_dir * t1
            return np.linalg.norm(intersection - path[t1]) <= r
        
        # Generate points along the path
        num_points = 100
        path = [start + t * alex_dir for t in np.linspace(0, 1, num_points)]
        
        # Check if the path intersects with either door
        return not (is_intersecting(path, np.array([x1, 0]), door1_dir) or
                   is_intersecting(path, np.array([x2, 0]), door2_dir))
    
    # Binary search for the maximum r
    low, high = 0, R
    while low < high:
        mid = (low + high + 1) // 2
        if check_path(mid):
            low = mid
        else:
            high = mid - 1
    
    return low

# Read input
R, l, w = map(int, input().split())
T = int(input())

for _ in range(T):
    A, B = map(float, input().split())
    result = can_reach_bob(R, l, w, A, B)
    print(result)
# Generator time: 42.4658 seconds