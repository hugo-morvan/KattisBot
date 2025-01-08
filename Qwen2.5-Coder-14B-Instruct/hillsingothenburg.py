import heapq

def dijkstra(n, start, heights, graph):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in graph[current_node]:
            height_difference = max(0, heights[current_node] - heights[neighbor])
            distance = current_distance + height_difference
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    n, m = map(int, input().split())
    start, end = map(int, input().split())
    heights = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    
    distances = dijkstra(n, start, heights, graph)
    print(distances[end])

if __name__ == "__main__":
    main()
# Generator time: 35.5842 seconds