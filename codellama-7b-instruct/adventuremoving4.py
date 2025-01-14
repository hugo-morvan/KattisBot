def solution(distance):
    if distance >= 200:
        return "Impossible"
    elif distance == 0 or distance == 1:
        return 0
    else:
        gas_station_prices = []
        total_cost = 0
        
        while len(gas_station_prices) < 2:
            gas_station_prices.append(int(input()))
            
        for i in range(len(gas_station_prices) - 1):
            if distance > gas_station_prices[i+1][0]:
                total_cost += (distance - gas_station_prices[i][0]) * gas_station_prices[i][1] / 10
                distance = gas_station_prices[i+1][0]
            else:
                total_cost += distance * gas_station_prices[i][1] / 10
                break
                
        if len(gas_station_prices) == 2 and distance < gas_station_prices[1][0]:
            return (gas_station_prices[1][0] - distance) * gas_station_prices[1][1] / 10 + total_cost
        else:
            total_cost += (distance - gas_station_prices[-2][0]) * gas_station_prices[-1][1] / 10
            return total_cost
# Generator time: 10.6191 seconds