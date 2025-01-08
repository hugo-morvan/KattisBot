# Read input values
n = int(input())
flights = []
for _ in range(n):
    flights.append(list(map(int, input().split())))

# Collect all direct flights and their costs
direct_flights = []
for i in range(n):
    for j in range(i + 1, n):
        if flights[i][j] != -1:
            direct_flights.append((i + 1, j + 1, flights[i][j]))
        if i != j and flights[j][i] != -1:
            direct_flights.append((j + 1, i + 1, flights[j][i]))

# Sort the list of direct flights by departure city, then by arrival city
direct_flights.sort()

# Output the number of direct flights
m = len(direct_flights)
print(m)

# Output each direct flight
for u, v, c in direct_flights:
    print(u, v, c)
# Generator time: 7.1892 seconds