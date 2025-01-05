import math

def min_distance(W):
    min_dist = float('inf')
    
    # Iterate over a range of times from 0 to W
    for t in range(int(W * 1000), int((W + 1e-9) * 1000)):
        t /= 1000  # Convert back to seconds
        
        # Calculate angles
        theta_A = t
        theta_B = 2 * t
        
        # Calculate distances
        dist = abs(math.cos(theta_B) - math.cos(theta_A))
        
        # Update minimum distance
        if dist < min_dist:
            min_dist = dist
    
    return min_dist

# Read input
W = float(input())

# Calculate and print the minimum distance
print(min_distance(W))
# Generator time: 25.7375 seconds