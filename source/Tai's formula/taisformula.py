def calculate_area(N):
    # Read the number of glucose samples
    N = int(input())
    
    # Initialize variables to store the area
    area = 0
    
    # Read the glucose samples
    for _ in range(N):
        t, v = map(float, input().split())
        
        # Calculate the area for each segment of the curve
        if area == 0:
            area += (v + v) * (t - 0)
        else:
            area += (v + v_prev) * (t - t_prev)
        
        # Update previous time and glucose value
        t_prev = t
        v_prev = v
    
    # Convert the area from mmol/L·ms to mmol/L·s
    area /= 1000
    
    # Print the result
    print(area)

# Call the function with the number of test cases
calculate_area(1)