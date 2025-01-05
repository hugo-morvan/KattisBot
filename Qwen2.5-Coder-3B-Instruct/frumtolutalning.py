def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(a, b):
    count = 0
    for num in range(max(2, a), b + 1):
        if is_prime(num):
            count += 1
    return count

# Read input
a, b = map(int, input().split())

# Calculate the number of primes in the range [a, b]
result = count_primes_in_range(a, b)

# Output the result
print(result)
# Generator time: 6.7348 seconds