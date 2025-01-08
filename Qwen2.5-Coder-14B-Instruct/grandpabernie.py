from collections import defaultdict

n = int(input())
trips = []

for _ in range(n):
    country, year = input().split()
    trips.append((country, int(year)))

q = int(input())
queries = []

for _ in range(q):
    country, k = input().split()
    queries.append((country, int(k)))

# Dictionary to store trips by country
country_trips = defaultdict(list)

for country, year in trips:
    country_trips[country].append(year)

# Sort the trips for each country by year
for country in country_trips:
    country_trips[country].sort()

# Process each query
for country, k in queries:
    # Since k is 1-indexed, we need to access index k-1
    print(country_trips[country][k-1])
# Generator time: 25.5043 seconds