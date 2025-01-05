import math

def find_k(x, y_low, y_high):
    # Initialize k
    k = 0
    
    # Apply the curving function until the result is within the desired range
    while True:
        y = math.ceil(10 * math.sqrt(x))
        if y >= y_low and y <= y_high:
            break
        if y > y_high:
            return "impossible"
        k += 1
        x = y
    
    # Check if we can apply the function an infinite number of times
    if y == y_high:
        return "inf", k
    else:
        return "impossible"

# Read input
x, y_low, y_high = map(int, input().split())

# Find the minimum and maximum k
min_k, max_k = find_k(x, y_low, y_high)

# Print the result
print(min_k, max_k)
# Generator time: 12.1417 seconds