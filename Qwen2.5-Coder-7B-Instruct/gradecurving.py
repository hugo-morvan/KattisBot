import math

def curve_score(x, y_low, y_high):
    f = lambda x: 10 * math.sqrt(x)
    k_min = 0
    k_max = 0
    y = round(f(x))
    
    while y < y_low:
        k_min += 1
        y = round(f(y))
    
    if y > y_high:
        return "impossible"
    
    while y <= y_high:
        k_max += 1
        y = round(f(y))
    
    return f"{k_min} {k_max}"

# Read input
input_line = input()
x, y_low, y_high = map(int, input_line.split())

# Output the result
print(curve_score(x, y_low, y_high))
# Generator time: 6.3139 seconds