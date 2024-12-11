# Read input
n = int(input())
at_bats = list(map(int, input().split()))

# Calculate total bases and official at-bats
total_bases = sum(at_bats)
official_at_bats = total_bases - at_bats.count(-1)

# Calculate slugging percentage
slugging_percentage = total_bases / official_at_bats

# Print the result
print(slugging_percentage)