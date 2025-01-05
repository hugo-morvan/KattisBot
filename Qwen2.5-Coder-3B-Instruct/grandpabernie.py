from collections import defaultdict

def find_trip_year(n, trips, q, queries):
    # Create a dictionary to store the trips for each country
    country_trips = defaultdict(list)
    
    # Populate the dictionary with trips
    for country, year in trips:
        country_trips[country].append(year)
    
    # Process each query
    for country, k in queries:
        # Sort the years for the country in ascending order
        country_trips[country].sort()
        # Output the k-th trip year
        print(country_trips[country][k-1])

# Read input
n = int(input())
trips = [input().split() for _ in range(n)]
q = int(input())
queries = [input().split() for _ in range(q)]

# Call the function to find the trip year for each query
find_trip_year(n, trips, q, queries)
# Generator time: 8.8092 seconds