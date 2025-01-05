import math

def is_perfect_square(n):
    root = int(math.isqrt(n))
    return root * root == n

def count_factorable_b(a, c):
    max_delta = 4 * a * c
    max_k = int(math.isqrt(max_delta))
    
    count = 0
    for b in range(max_k + 1):
        delta = b * b - 4 * a * c
        if is_perfect_square(delta):
            count += 1
    
    return count

# Read input
a, c = map(int, input().split())

# Calculate and print the result
print(count_factorable_b(a, c))
# Generator time: 28.4799 seconds