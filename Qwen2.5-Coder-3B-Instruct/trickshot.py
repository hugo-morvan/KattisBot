import math

def calculate_shot(w, l, h, r, x1, y1, x2, y2, x3, y3):
    # Calculate the center of the table
    table_center_x = w / 2
    table_center_y = l
    
    # Calculate the center of the holes
    hole1_center = (0, l)
    hole2_center = (w, l)
    
    # Calculate the center of the cue ball
    cue_ball_center = (table_center_x, h + r)
    
    # Calculate the vector from the cue ball to the center of ball 1
    vec_cue_to_ball1 = (x1 - cue_ball_center[0], y1 - cue_ball_center[1])
    
    # Calculate the vector from the cue ball to the center of ball 2
    vec_cue_to_ball2 = (x2 - cue_ball_center[0], y2 - cue_ball_center[1])
    
    # Calculate the vector from the cue ball to the center of ball 3
    vec_cue_to_ball3 = (x3 - cue_ball_center[0], y3 - cue_ball_center[1])
    
    # Calculate the vector from the center of ball 1 to the center of ball 2
    vec_ball1_to_ball2 = (x2 - x1, y2 - y1)
    
    # Calculate the vector from the center of ball 2 to the center of ball 3
    vec_ball2_to_ball3 = (x3 - x2, y3 - y2)
    
    # Calculate the dot product of vec_cue_to_ball1 and vec_ball1_to_ball2
    dot_product1 = vec_cue_to_ball1[0] * vec_ball1_to_ball2[0] + vec_cue_to_ball1[1] * vec_ball1_to_ball2[1]
    
    # Calculate the dot product of vec_cue_to_ball2 and vec_ball2_to_ball3
    dot_product2 = vec_cue_to_ball2[0] * vec_ball2_to_ball3[0] + vec_cue_to_ball2[1] * vec_ball2_to_ball3[1]
    
    # Calculate the magnitudes of the vectors
    magnitude_cue_to_ball1 = math.sqrt(vec_cue_to_ball1[0]**2 + vec_cue_to_ball1[1]**2)
    magnitude_vec_ball1_to_ball2 = math.sqrt(vec_ball1_to_ball2[0]**2 + vec_ball1_to_ball2[1]**2)
    magnitude_vec_ball2_to_ball3 = math.sqrt(vec_ball2_to_ball3[0]**2 + vec_ball2_to_ball3[1]**2)
    
    # Calculate the cosine of the angles between the vectors
    cos_theta1 = dot_product1 / (magnitude_cue_to_ball1 * magnitude_vec_ball1_to_ball2)
    cos_theta2 = dot_product2 / (magnitude_cue_to_ball2 * magnitude_vec_ball2_to_ball3)
    
    # Calculate the angles in radians
    theta1_rad = math.acos(cos_theta1)
    theta2_rad = math.acos(cos_theta2)
    
    # Convert angles to degrees
    theta1_deg = math.degrees(theta1_rad)
    theta2_deg = math.degrees(theta2_rad)
    
    # Check if the angles are valid
    if theta1_deg < 0 or theta1_deg > 90 or theta2_deg < 0 or theta2_deg > 90:
        return "impossible"
    
    # Calculate the distance d
    d = math.sqrt((cue_ball_center[0] - hole1_center[0])**2 + (cue_ball_center[1] - hole1_center[1])**2)
    
    # Round the distance and angle to the nearest hundredth
    d_rounded = round(d, 2)
    theta1_rounded = round(theta1_deg, 2)
    theta2_rounded = round(theta2_deg, 2)
    
    # Return the result
    return f"{d_rounded} {theta1_rounded} {theta2_rounded}"

# Read input
w, l = map(int, input().split())
r = int(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
h = float(input())

# Calculate the result
result = calculate_shot(w, l, h, r, x1, y1, x2, y2, x3, y3)

# Print the result
print(result)
# Generator time: 47.2765 seconds