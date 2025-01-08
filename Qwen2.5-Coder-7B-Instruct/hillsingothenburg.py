import heapq

def dijkstra(n, m, start, end, heights, roads):
    graph = [[] for _ in range(n + 1)]
    for i, j in roads:
        height_diff = abs(heights[i - 1] - heights[j - 1])
        graph[i].append((j, height_diff))
        graph[j].append((i, height_diff))

    min_heap = [(0, start)]
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    while min_heap:
        current_distance, node = heapq.heappop(min_heap)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances[end]

def main():
    n, m = map(int, input().split())
    start, end = map(int, input().split())
    heights = list(map(int, input().split()))
    roads = [tuple(map(int, input().split())) for _ in range(m)]

    result = dijkstra(n, m, start, end, heights, roads)
    print(result)

if __name__ == "__main__":
    main()
# Generator time: 11.0753 seconds