# Read input values
X = int(input())
N = int(input())
spent = [int(input()) for _ in range(N)]

# Calculate the remaining megabytes available in the N+1 month
remaining = X - sum(spent)

# Output the result
print(remaining)