def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Read input values
A = int(input())
B = int(input())

# Compute the GCD
result = gcd(A, B)

# Output the result
print(result)