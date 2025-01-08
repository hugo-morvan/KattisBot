def min_gas_cost(distance, stations):
    # Initial conditions
    tank_capacity = 200
    initial_fuel = tank_capacity // 2
    current_fuel = initial_fuel
    current_position = 0
    total_cost = 0

    # Add a dummy station at the end to handle the destination
    stations.append((distance, float('inf')))

    for pos, price in stations:
        if pos > distance:
            break

        # Drive to the next station or destination
        while current_position < pos and current_fuel > 0:
            current_position += 1
            current_fuel -= 1

        # If we run out of gas before reaching the next station
        if current_fuel == 0:
            return "Impossible"

        # Refuel optimally at the current station
        refuel_amount = min(tank_capacity // 2 - current_fuel, pos - current_position)
        total_cost += refuel_amount * price
        current_fuel += refuel_amount

    return total_cost

# Read input
distance = int(input())
stations = []
for _ in range(int(input())):
    d, p = map(int, input().split())
    stations.append((d, p))

# Calculate and print the result
print(min_gas_cost(distance, stations))
# Generator time: 36.5355 seconds