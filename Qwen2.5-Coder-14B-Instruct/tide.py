import heapq

def dijkstra_with_water_level(H, N, M, ceilings, floors):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    end = (N-1, M-1)
    
    # Priority queue for Dijkstra's algorithm
    pq = []
    # Distance dictionary to store the minimum time to reach each cell
    dist = {(i, j): float('inf') for i in range(N) for j in range(M)}
    dist[start] = 0
    
    # Push start into the priority queue
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_time, (x, y) = heapq.heappop(pq)
        
        if (x, y) == end:
            return current_time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # Water level condition
                water_level_condition = H - current_time * 10 - floors[nx][ny] >= 50
                # Floor height condition
                floor_height_condition = ceilings[x][y] - floors[nx][ny] >= 50
                # Ceiling height condition
                ceiling_height_condition = ceilings[nx][ny] - floors[nx][ny] >= 50
                
                if water_level_condition and floor_height_condition and ceiling_height_condition:
                    new_time = current_time + (10 if H - current_time * 10 - floors[x][y] < 20 else 1)
                    
                    if new_time < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_time
                        heapq.heappush(pq, (new_time, (nx, ny)))
    
    return float('inf')

def main():
    T = int(input())
    for case in range(1, T + 1):
        H, N, M = map(int, input().split())
        ceilings = [list(map(int, input().split())) for _ in range(N)]
        floors = [list(map(int, input().split())) for _ in range(N)]
        
        result = dijkstra_with_water_level(H, N, M, ceilings, floors)
        print(f"Case #{case}: {result:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 75.1239 seconds