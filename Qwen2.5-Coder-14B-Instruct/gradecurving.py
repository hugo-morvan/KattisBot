import math

def curve_score(x, y_low, y_high):
    def f(x):
        return 10 * math.sqrt(x)
    
    k_min = float('inf')
    k_max = 0
    
    current_score = x
    for k in range(21):  # Since the score is out of 100, applying more than 20 times will exceed 100
        current_score = f(current_score)
        rounded_score = math.ceil(current_score)
        
        if y_low <= rounded_score <= y_high:
            k_min = min(k_min, k)
            k_max = max(k_max, k)
        
        if rounded_score > y_high:
            break
    
    if k_min == float('inf'):
        return "impossible"
    
    if k_max == 20:  # If we reach the limit and still valid, it means it can be applied infinitely
        k_max = "inf"
    
    return k_min, k_max

x, y_low, y_high = map(int, input().split())
result = curve_score(x, y_low, y_high)
if isinstance(result, str):
    print(result)
else:
    print(result[0], result[1])
# Generator time: 36.0472 seconds