def min_man_hours_to_build_bridges():
    T = int(input())
    results = []
    
    for _ in range(T):
        N, M = map(int, input().split())
        grid = [input() for _ in range(N)]
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def is_valid(x, y):
            return 0 <= x < N and 0 <= y < M
        
        def bfs(start):
            queue = [start]
            visited = set([start])
            distance = {start: 0}
            
            while queue:
                x, y = queue.pop(0)
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        distance[(nx, ny)] = distance[(x, y)] + 1
                        queue.append((nx, ny))
            
            return distance
        
        # Find all forests and calculate distances from the base camp
        forest_distances = bfs((0, 0))
        
        # Calculate the minimum man-hours to connect all islands
        total_hours = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '#':
                    min_distance = float('inf')
                    for x in range(N):
                        for y in range(M):
                            if (x, y) in forest_distances:
                                min_distance = min(min_distance, forest_distances[(x, y)] + abs(i - x) + abs(j - y))
                    total_hours += min_distance
        
        results.append(f"Case #{_ + 1}: {total_hours}")
    
    for result in results:
        print(result)

min_man_hours_to_build_bridges()
# Generator time: 12.2336 seconds