# Read input values
n, k = map(int, input().split())
bags = list(map(int, input().split()))

# Find the index of Benni's bag
index = bags.index(k)

# Determine how first Benni's bag is
if index == 0:
    result = "fyrst"
elif index == 1:
    result = "naestfyrst"
else:
    result = str(index) + " fyrst"

# Print the result
print(result)