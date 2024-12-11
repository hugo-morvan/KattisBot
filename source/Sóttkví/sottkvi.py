# Read input values
n, k, d = map(int, input().split())
quarantine_days = list(map(int, input().split()))

# Count how many friends will make it to the party
friends_making_it = sum(1 for day in quarantine_days if day + k <= d)

# Print the result
print(friends_making_it)