def min_days_to_next_name_day(friend_name, name_days):
    min_days = float('inf')
    
    for name_day in name_days:
        # Count the differences between the friend's name and the name day
        diff_count = sum(1 for char1, char2 in zip(friend_name, name_day) if char1 != char2)
        
        # If exactly one character differs, update the minimum days
        if diff_count == 1:
            min_days = min(min_days, name_days.index(name_day))
    
    return min_days

# Read input
friend_name = input()
n = int(input())
name_days = [input() for _ in range(n)]

# Calculate and print the result
result = min_days_to_next_name_day(friend_name, name_days)
print(result)