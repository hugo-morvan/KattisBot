import heapq

def can_move(current, next_square, water_level):
    current_ceiling, current_floor = current
    next_ceiling, next_floor = next_square
    
    if (water_level < current_ceiling - 50 and
        water_level < next_ceiling - 50 and
        next_floor >= water_level + 50 and
        next_floor <= current_floor):
        return True
    return False

def calculate_time():
    T = int(input())
    
    for test_case in range(1, T + 1):
        H, N, M = map(int, input().split())
        
        ceiling_heights = []
        floor_heights = []
        
        for _ in range(N):
            row = list(map(int, input().split()))
            ceiling_heights.append(row)
            
        for _ in range(N):
            row = list(map(int, input().split()))
            floor_heights.append(row)
        
        start_time = 0
        water_level = H
        
        if H > 50:
            start_time += (H - 50) / 10
        
        queue = []
        heapq.heappush(queue, (start_time + max(0, ceiling_heights[0][0] - water_level - 20), 0, 0))
        
        visited = set()
        visited.add((0, 0))
        
        while queue:
            time, x, y = heapq.heappop(queue)
            
            if (x, y) == (N-1, M-1):
                print(f"Case #{test_case}: {time:.6f}")
                break
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                    current_square = (ceiling_heights[x][y], floor_heights[x][y])
                    next_square = (ceiling_heights[nx][ny], floor_heights[nx][ny])
                    
                    if can_move(current_square, next_square, water_level):
                        new_time = time + (max(0, ceiling_heights[x][y] - water_level - 20) / 10)
                        heapq.heappush(queue, (new_time, nx, ny))
                        visited.add((nx, ny))

calculate_time()
# Generator time: 16.0898 seconds