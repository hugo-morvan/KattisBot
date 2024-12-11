def enough_sanitizer(n, x, a):
    # Check if the total sanitizer needed is less than or equal to the available sanitizer
    if sum(a) <= x:
        return "Jebb"
    else:
        return "Neibb"

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the result
result = enough_sanitizer(n, x, a)
print(result)