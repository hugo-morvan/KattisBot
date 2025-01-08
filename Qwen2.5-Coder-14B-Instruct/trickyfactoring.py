import math

def count_factorable_b_values(a, c):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # Calculate the discriminant of the quadratic equation ax^2 + bx + c = 0
    # The discriminant is b^2 - 4ac
    # For the quadratic to be factorable over integers, the discriminant must be a perfect square
    # Let's denote the discriminant by D = k^2 where k is an integer
    
    # We need to find all possible values of b such that b^2 - 4ac = k^2 for some integer k
    # Rearranging gives us b^2 - k^2 = 4ac
    # This can be factored as (b - k)(b + k) = 4ac
    
    count = 0
    limit = int(math.sqrt(4 * a * c)) + 1
    
    for k in range(limit):
        if (k * k) % 4 == 0:  # Check if k^2 is divisible by 4
            D = k * k
            # We need to find pairs (m, n) such that m * n = 4ac and m + n = b - k and m - n = b + k
            # This means b = (m + n) / 2 and b must be an integer
            product = 4 * a * c
            for m in range(1, int(math.sqrt(product)) + 1):
                if product % m == 0:
                    n = product // m
                    if (m + n) % 2 == 0:
                        count += 1
    
    return count

a, c = map(int, input().split())
print(count_factorable_b_values(a, c))
# Generator time: 50.7185 seconds