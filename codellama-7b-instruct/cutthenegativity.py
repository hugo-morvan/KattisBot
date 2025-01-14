n = int(input())
flight_dict = {}
for i in range(n):
    flight_list = list(map(int, input().split()))
    for j in range(1, n + 1):
        if (flight_list[j] != -1):
            flight_dict[(i+1, j)] = [j, i+1, flight_list[j]]
sorted_flights = sorted(flight_dict.values(), key = lambda x: (x[0], x[2]))
print(len(sorted_flights))
for flight in sorted_flights:
    print(flight[0], flight[1], flight[2])
# Generator time: 5.9072 seconds