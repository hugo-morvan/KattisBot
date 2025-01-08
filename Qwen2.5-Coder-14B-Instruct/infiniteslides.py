import math

def calculate_min_distance(W):
    # Constants for Agneta's slide
    agneta_speed_vertical = 1
    agneta_speed_angular = 1
    
    # Constants for Beata's slide
    beata_speed_vertical = 2
    beata_speed_angular = 1
    
    # Time when Beata starts her descent
    t_beata_start = W
    
    # Initial positions
    agneta_position = (1, 0)
    beata_position = (2 + W * beata_speed_angular, W * beata_speed_vertical)
    
    min_distance = float('inf')
    
    # Simulate the slides for a reasonable amount of time
    t_max = 1000  # seconds
    dt = 0.01  # small time step
    
    for t in range(0, int(t_max / dt) + 1):
        t_current = t * dt
        
        # Calculate Agneta's position at current time
        agneta_angle = agneta_speed_angular * t_current
        agneta_x = math.cos(agneta_angle)
        agneta_y = math.sin(agneta_angle)
        
        # Calculate Beata's position at current time
        if t_current >= t_beata_start:
            beata_angle = beata_speed_angular * (t_current - t_beata_start)
            beata_x = 2 + beata_angle
            beata_y = beata_speed_vertical * (t_current - t_beata_start)
        
        # Calculate Euclidean distance between Agneta and Beata
        distance = math.sqrt((agneta_x - beata_x) ** 2 + (agneta_y - beata_y) ** 2)
        
        # Update minimum distance
        if distance < min_distance:
            min_distance = distance
    
    return min_distance

# Read input
W = float(input().strip())

# Calculate and print the minimal Euclidean distance
print(f"{calculate_min_distance(W):.6f}")
# Generator time: 55.4993 seconds