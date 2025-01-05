def min_processing_time(s, t, blades):
    # Sort blades by maximum average piece size in descending order
    blades.sort(key=lambda x: x[0], reverse=True)
    
    current_size = s
    time = 0
    
    for m, h in blades:
        if current_size <= m:
            continue
        # Calculate the time required to halve the current size
        time += h
        current_size /= 2
        
        # Check if the target size is reached
        if current_size <= t:
            break
    
    # If the target size is not reached, return -1
    if current_size > t:
        return -1
    
    return time

# Read input
s, t, n = map(int, input().split())
blades = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_processing_time(s, t, blades))
# Generator time: 24.3403 seconds