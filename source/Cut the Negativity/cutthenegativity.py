def process_flights():
    n = int(input())
    flights = [list(map(int, input().split())) for _ in range(n)]
    
    # Find direct flights
    direct_flights = []
    for i in range(n):
        for j in range(n):
            if flights[i][j] != -1:
                direct_flights.append((i + 1, j + 1, flights[i][j]))
    
    # Sort direct flights by departure city, then by arrival city
    direct_flights.sort(key=lambda x: (x[0], x[1]))
    
    # Output the number of direct flights
    print(len(direct_flights))
    
    # Output the list of direct flights
    for flight in direct_flights:
        print(f"{flight[0]} {flight[1]} {flight[2]}")

# Process the flights
process_flights()