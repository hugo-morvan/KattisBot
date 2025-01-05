def process_flights():
    import sys

    # Read input
    n = int(input())
    flights = [list(map(int, input().split())) for _ in range(n)]

    # Collect valid flights
    valid_flights = []
    for i in range(n):
        for j in range(n):
            if flights[i][j] != -1:
                valid_flights.append((i + 1, j + 1, flights[i][j]))

    # Sort valid flights by departure city and then arrival city
    valid_flights.sort(key=lambda x: (x[0], x[1]))

    # Print the number of valid flights
    print(len(valid_flights))

    # Print each valid flight
    for flight in valid_flights:
        print(f"{flight[0]} {flight[1]} {flight[2]}")

# Call the function
process_flights()
# Generator time: 9.9033 seconds