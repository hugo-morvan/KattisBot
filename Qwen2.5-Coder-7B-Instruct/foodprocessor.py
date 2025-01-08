def min_processing_time(s, t, n):
    blades = []
    for _ in range(n):
        m, h = map(int, input().split())
        blades.append((m, h))
    
    # Sort blades by their maximum piece size in ascending order
    blades.sort(key=lambda x: x[0])
    
    time_needed = 0
    current_size = s
    
    for m, h in blades:
        if current_size <= t:
            break
        
        if current_size > m:
            return -1
        
        # Calculate the number of times we need to use this blade
        reductions = (current_size / m).bit_length() - 1
        time_needed += reductions * h
        current_size /= 2 ** reductions
    
    if current_size <= t:
        return time_needed
    else:
        return -1

# Read input
s, t, n = map(int, input().split())

# Calculate and print the result
print(min_processing_time(s, t, n))
# Generator time: 7.4007 seconds