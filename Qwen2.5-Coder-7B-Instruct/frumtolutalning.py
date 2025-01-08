def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(a, b):
    prime_count = 0
    for num in range(a, b + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count

# Read input
a, b = map(int, input().split())

# Output the result
print(count_primes_in_range(a, b))
# Generator time: 6.2623 seconds