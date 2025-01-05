import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == end:
            return current_distance
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return float('inf')

def main():
    # Read input
    N, M = map(int, input().split())
    start, end = map(int, input().split())
    heights = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    
    for _ in range(M):
        i, j = map(int, input().split())
        graph[i-1].append((j-1, heights[j-1] - heights[i-1]))
        graph[j-1].append((i-1, heights[i-1] - heights[j-1]))
    
    # Calculate the minimum uphill distance
    min_uphill_distance = dijkstra(graph, start-1, end-1)
    
    # Output the result
    print(min_uphill_distance)

if __name__ == "__main__":
    main()
# Generator time: 22.0768 seconds