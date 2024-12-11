import math

def calculate_trajectory(v0, theta, x1, h1, h2):
    theta_rad = math.radians(theta)
    g = 9.81
    
    # Calculate the time of flight
    t_flight = (2 * v0 * math.sin(theta_rad)) / g
    
    # Calculate the horizontal distance traveled
    x_final = v0 * t_flight * math.cos(theta_rad)
    
    # Calculate the maximum height reached
    max_height = (v0 * math.sin(theta_rad))**2 / (2 * g)
    
    # Calculate the vertical position at the centerline of the wall
    centerline_y = h1 + (h2 - h1) / 2
    
    # Check if the cannonball passes through the centerline with a safety margin
    if x_final >= x1 and centerline_y <= max_height:
        return True
    else:
        return False

# Read input
N = int(input())
results = []

for _ in range(N):
    v0, theta, x1, h1, h2 = map(float, input().split())
    if calculate_trajectory(v0, theta, x1, h1, h2):
        results.append("Safe")
    else:
        results.append("Not Safe")

# Print results
for result in results:
    print(result)