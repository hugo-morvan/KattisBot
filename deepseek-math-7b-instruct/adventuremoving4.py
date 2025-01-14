 def min_gas_cost(distance, stations):
    # Initialize minimum cost with infinity (a large number) and tank capacity as half full at start point
    current = distance / 200; remainingDistance = distance ;minCost=float("inf")
    for station in sorted(stations, key=lambda x:x[1]) :# Sort stations by increasing price per litre of gas.
        if (station[0] - nextStation) > current or len(stations)== 2+nextStation<distance:# If the distance to this station is more than we can go with our remaining fuel, skip it and move onto Next Station   :continue;current = max((remainingDistance-station [1])/5 ,.0); # calculate how much gas from current position will reach till next station
        minCost=min( (max(.4,(2*stations[i][3]- stations[(j)%len([ i for j in range(- 8, - len([]),- 1):]))]if((station [0])-(nextStation))>current else float("inf")) ),
            minCost); # If the distance to this station is more than we can go with our remaining fuel or if there are no stations left then calculate cost from current position till end of trip. Else select minimum between two options(both will give same ans).
# Generator time: 8.7706 seconds