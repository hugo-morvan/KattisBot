def find_temperature_range():
    # Read the number of people
    N = int(input())
    
    # Initialize variables to store the minimum and maximum preferences
    min_preference = float('inf')
    max_preference = float('-inf')
    
    # Parse the input preferences
    for _ in range(N):
        a, b = map(int, input().split())
        min_preference = min(min_preference, a)
        max_preference = max(max_preference, b)
    
    # Check if there is a valid temperature
    if min_preference > max_preference:
        print("bad news")
    else:
        # The number of valid temperatures is the difference + 1
        num_valid_temperatures = max_preference - min_preference + 1
        print(num_valid_temperatures, min_preference)

# Call the function to find the temperature range
find_temperature_range()
# Generator time: 19.7964 seconds