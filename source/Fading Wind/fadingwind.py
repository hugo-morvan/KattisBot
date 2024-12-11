import math

def calculate_horizontal_distance(h, k, v, s):
    while h > 0:
        v += s
        v = max(1, math.floor(v / 10))
        
        if v >= k:
            h += 1
        elif 0 < v < k:
            h -= 1
            if h == 0:
                v = 0
        else:
            h = 0
            v = 0
        
        s -= 1
    
    return v

# Read input
h, k, v, s = map(int, input().split())

# Calculate and print the horizontal distance
print(calculate_horizontal_distance(h, k, v, s))