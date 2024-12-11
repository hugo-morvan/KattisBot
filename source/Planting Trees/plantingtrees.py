# Read the number of seedlings
n = int(input())

# Read the growth times for each tree
growth_times = list(map(int, input().split()))

# Sort the growth times in ascending order
growth_times.sort()

# The earliest day for the party is the maximum growth time plus one
earliest_day = max(growth_times) + 1

# Output the earliest day
print(earliest_day)