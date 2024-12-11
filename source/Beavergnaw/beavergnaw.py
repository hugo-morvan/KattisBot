import math

while True:
    D, V = map(int, input().split())
    if D == 0 and V == 0:
        break
    
    # Volume of the frustum of the cone
    def frustum_volume(D, d):
        return (math.pi * D * d * (D - d)) / 3
    
    # Volume of the cylinder
    def cylinder_volume(d):
        return math.pi * d ** 2 * D
    
    # Total volume to be chomped
    total_volume = V
    
    # Binary search to find the optimal diameter d
    low, high = 0, D
    while low < high:
        mid = (low + high) // 2
        volume = frustum_volume(D, mid) + cylinder_volume(mid)
        
        if volume > total_volume:
            high = mid
        else:
            low = mid + 1
    
    # The final value of d
    d = low
    
    # Print the result rounded to 6 decimal places
    print(f"{d:.6f}")