def cookies(N, A):
    total_cookies = sum(A)
    return total_cookies

# Read input values
N = int(input())
A = list(map(int, input().split()))

# Calculate the total number of cookies
result = cookies(N, A)

# Print the result
print(result)