def count_friday_13ths(D, M, d):
    # Initialize the day of the week for the first day of the year
    day_of_week = 0  # 0 represents Sunday, 1 represents Monday, ..., 6 represents Saturday
    
    # Iterate through each month
    for days_in_month in d:
        # Add the number of days in the current month to the day of the week
        day_of_week = (day_of_week + days_in_month) % 7
        
        # Check if the 13th falls on a Friday (day_of_week == 5)
        if day_of_week == 5:
            # Count a Friday the 13th
            friday_13ths_count += 1
    
    return friday_13ths_count

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the total number of days and months in the year
    D, M = map(int, input().split())
    
    # Read the number of days in each month
    d = list(map(int, input().split()))
    
    # Calculate the number of Friday the 13ths
    friday_13ths_count = count_friday_13ths(D, M, d)
    
    # Output the result
    print(friday_13ths_count)
# Generator time: 20.9742 seconds