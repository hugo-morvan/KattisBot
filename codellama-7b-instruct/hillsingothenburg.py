from collections import defaultdict
import heapq

def solve(n_spots, n_roads, start_smurf, end_smurf, spots):
    graph = defaultdict(list)
    
    for i in range(1, n_roads+1):
        x, y = map(int, input().split())
        graph[x].append((y, abs(spots[y] - spots[x])))
        
    dist = [float('inf') for _ in range(n_spots+1)]
    
    heapq.heappush(dist, start_smurf)
    
    while dist:
        node = heapq.heappop(dist)
        
        if dist[node] == 0:
            continue
            
        for child in graph[node]:
            new_distance = dist[node] + child[1]
            if new_distance < dist[child[0]]:
                heapq.heappush(dist, child[0])
                dist[child[0]] = new_distance
                
    return dist[end_smurf]
# Generator time: 8.1395 seconds