def min_gas_cost():
    distance_to_city = int(input())
    num_stations = int(input())
    
    if distance_to_city > 200:
        return "Impossible"
    
    stations = []
    for _ in range(num_stations):
        station_distance, gas_price = map(int, input().split())
        stations.append((station_distance, gas_price))
    
    # Calculate the minimum cost to reach the city
    tank_size = 200
    current_gas = 100  # Starting with half a tank in litres
    total_cost = 0
    
    for i in range(num_stations + 1):
        if i < num_stations:
            next_station_distance, _ = stations[i]
        else:
            next_station_distance = distance_to_city
        
        if current_gas >= (next_station_distance - 0) / 100 * tank_size:
            continue
        
        required_gas = (next_station_distance - 0) / 100 * tank_size - current_gas
        min_price = float('inf')
        
        for station in stations:
            if station[0] <= next_station_distance and station[1] < min_price:
                min_price = station[1]
        
        if min_price == float('inf'):
            return "Impossible"
        
        total_cost += required_gas * min_price / 100
        current_gas = tank_size
    
    # Check if we can reach the city with the remaining gas
    if current_gas >= (distance_to_city - 0) / 100 * tank_size:
        return f"{total_cost:.2f}"
    else:
        return "Impossible"

print(min_gas_cost())
# Generator time: 10.6776 seconds