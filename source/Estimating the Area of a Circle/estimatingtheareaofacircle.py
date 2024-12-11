import math

def estimate_circle_area(r, m, c):
    # Calculate the true area of the circle
    true_area = math.pi * r**2
    
    # Estimate the area using the ratio of points in the circle to total points
    estimate = (c / m) * true_area
    
    return true_area, estimate

# Read input
while True:
    line = input()
    if line == '0 0 0':
        break
    r, m, c = map(float, line.split())
    
    # Estimate the area
    true_area, estimate = estimate_circle_area(r, m, c)
    
    # Print the result
    print(f"{true_area:.6f} {estimate:.6f}")