import math

def max_digits(C):
    # Initial guess for n
    n = 1
    
    # Iterate until the condition is satisfied
    while True:
        if n * math.log10(n) <= C * 10**6:
            n += 1
        else:
            break
    
    # Return the previous value of n, which satisfies the condition
    return n - 1

# Read input
C = int(input())

# Calculate and print the result
print(max_digits(C))
# Generator time: 15.3856 seconds