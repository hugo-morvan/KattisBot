from collections import defaultdict

# Read input
n = int(input())
trips = [input().split() for _ in range(n)]
q = int(input())
queries = [input().split() for _ in range(q)]

# Create a dictionary to store trips by country
trip_dict = defaultdict(list)

# Populate the trip dictionary
for s, y in trips:
    trip_dict[s].append(int(y))

# Process each query and print the result
for s, k in queries:
    k = int(k) - 1  # Convert to 0-based index
    if 0 <= k < len(trip_dict[s]):
        year = trip_dict[s][k]
        print(year)
    else:
        print("Invalid query")
# Generator time: 6.1374 seconds