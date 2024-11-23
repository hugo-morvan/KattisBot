def find_common_temperatures():
    # Read the number of people
    N = int(input())
    
    # Initialize variables to store the minimum and maximum temperatures
    min_temp = float('inf')
    max_temp = float('-inf')
    
    # Read each person's temperature preference
    for _ in range(N):
        a, b = map(int, input().split())
        
        # Update the minimum and maximum temperatures
        min_temp = min(min_temp, a)
        max_temp = max(max_temp, b)
    
    # Check if there is an overlap
    if min_temp > max_temp:
        print("bad news")
    else:
        # Calculate the number of common temperatures
        num_common_temps = max_temp - min_temp + 1
        
        # Output the result
        print(num_common_temps, min_temp)

# Call the function to find common temperatures
find_common_temperatures()