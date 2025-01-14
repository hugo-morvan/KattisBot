n,m = map(int, input().split())
road_pairs = [map(int, input().split()) for _ in range(m)]
unique_sites = set()
for road in road_pairs:
    unique_sites.add(road[0])
    unique_sites.add(road[1])
possible_companies = []
num_routes = 0
min_num_routes = math.inf
for num_buses in range(2, len(unique_sites)+1):
    possible_companies.append([])
    for company in range(num_buses):
        possible_companies[company].append([])
    for road in road_pairs:
        if road[0] == road[1]: continue # skip the bidirectional roads
        for bus_route in range(len(road_pairs)):
            if len(possible_companies[bus_route][company]) < 2:
                possible_companies[bus_route][company].append([road])
            else:
                possible_companies[bus_route][company][1].append(road)
    for bus_route in range(len(road_pairs)):
        num_routes = 0
        for company in range(num_buses):
            if len(possible_companies[bus_route][company]) < 2:
                break
            elif len(possible_companies[bus_route][company]) == 2:
                num_routes += 1
        if num_routes > min_num_routes:
            possible_companies.pop()
            continue
        else:
            min_num_routes = num_routes
print(possible_companies)
# Generator time: 17.0710 seconds