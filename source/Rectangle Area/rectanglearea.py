import sys

def calculate_rectangle_area():
    # Read input values
    x1, y1, x2, y2 = map(float, input().split())
    
    # Calculate the width and height of the rectangle
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    # Calculate the area of the rectangle
    area = width * height
    
    # Print the area with 2 decimal places accuracy
    print(f"{area:.2f}")

# Call the function to solve the problem
calculate_rectangle_area()