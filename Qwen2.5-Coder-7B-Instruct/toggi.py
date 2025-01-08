import math

def max_digits(C):
    left, right = 1, C * 10**6
    while left < right:
        mid = (left + right) // 2
        if mid * math.log10(mid) / 10**6 <= C:
            left = mid + 1
        else:
            right = mid
    return left - 1

C = int(input())
print(max_digits(C))
# Generator time: 4.7967 seconds