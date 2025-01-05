def min_gas_cost(distance, gas_stations):
    # Initialize variables
    current_distance = 0
    gas_tank = 200
    total_cost = 0
    last_station = None

    while current_distance < distance:
        if gas_tank == 0:
            return "Impossible"
        
        # Find the nearest gas station
        nearest_station = None
        for station in gas_stations:
            if station[0] > current_distance:
                nearest_station = station
                break
        
        if nearest_station is None:
            return "Impossible"
        
        # Calculate the cost to reach the nearest station
        cost_to_station = (nearest_station[0] - current_distance) * nearest_station[1]
        total_cost += cost_to_station
        gas_tank -= (nearest_station[0] - current_distance)
        current_distance = nearest_station[0]

    # Check if the tank is at least half full when returning
    if gas_tank < 100:
        return "Impossible"

    return total_cost

# Read input
distance = int(input())
gas_stations = []
for _ in range(int(input())):
    station = tuple(map(int, input().split()))
    gas_stations.append(station)

# Calculate and print the result
print(min_gas_cost(distance, gas_stations))
# Generator time: 15.6000 seconds