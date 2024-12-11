def count_free_food_days(N):
    # Read input values
    events = []
    for _ in range(N):
        s, t = map(int, input().split())
        events.append((s, t))
    
    # Initialize a set to keep track of days with free food
    free_food_days = set()
    
    # Iterate through each event and add its days to the set
    for s, t in events:
        for day in range(s, t + 1):
            free_food_days.add(day)
    
    # Return the number of unique days with free food
    return len(free_food_days)

# Read the number of events
N = int(input())

# Calculate and print the result
print(count_free_food_days(N))