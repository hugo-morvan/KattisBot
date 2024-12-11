def can_make_it_to_class():
    # Parse input
    s, t, n = map(int, input().split())
    d = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    # Initialize variables
    total_time = 0
    
    # Calculate total time spent on buses and walking
    for i in range(n):
        # Time to walk from previous stop to current bus stop
        total_time += d[i]
        # Time spent on the current bus
        total_time += b[i]
        # Time to walk from current bus stop to next stop
        total_time += d[i + 1]
    
    # Total time spent including the first walk
    total_time += d[0]
    
    # Check if Yraglac arrives on time
    if total_time <= t:
        return "yes"
    else:
        return "no"

# Call the function and print the result
print(can_make_it_to_class())