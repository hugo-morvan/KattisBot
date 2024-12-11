# Read input values
n = int(input())
space_junk = list(map(int, input().split()))

# Find the minimum value in the list
min_space_junk = min(space_junk)

# Find the index of the minimum value
min_index = space_junk.index(min_space_junk)

# Calculate the number of days Birk has to wait
days_to_wait = n - min_index

# Output the result
print(days_to_wait)