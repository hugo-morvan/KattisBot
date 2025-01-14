def get_min_max(x, y_low, y_high):
    k = 0
    while f(k) < y_low:
        k += 1
    
    if y_high < f(k):
        return "impossible"
        
    max_k = k
    min_k = k - 1
    while min_k > 0 and y_low <= f(min_k) and f(min_k) < y_high:
        min_k -= 1
    
    if y_high == f(max_k):
        return "inf"
        
    return (min_k, max_k)
# Generator time: 44.8854 seconds