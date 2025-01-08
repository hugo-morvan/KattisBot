import math

def max_digits_of_pi(C):
    low, high = 1, int(1e6)  # Start with a reasonable upper bound
    while low < high:
        mid = (low + high + 1) // 2
        time_required = mid * math.log10(mid) / 1e6
        if time_required <= C:
            low = mid
        else:
            high = mid - 1
    return low

C = int(input())
print(max_digits_of_pi(C))
# Generator time: 16.9369 seconds