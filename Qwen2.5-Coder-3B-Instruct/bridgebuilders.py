def min_bridge_hours(grid):
    from collections import deque
    from heapq import heappush, heappop

    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col, 0)])
        visited = set()
        visited.add((start_row, start_col))
        while queue:
            row, col, hours = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < N and 0 <= new_col < M and grid[new_row][new_col] != '.' and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, hours + 1))
        return hours

    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]

    # Find the base camp (top left corner)
    base_row, base_col = 0, 0
    while grid[base_row][base_col] != 'T':
        base_row += 1
        base_col += 1

    # Calculate the minimum man-hours to connect all islands
    man_hours = 0
    visited = set()
    pq = []
    heappush(pq, (bfs(base_row, base_col), (base_row, base_col)))

    while pq:
        hours, (row, col) = heappop(pq)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        man_hours += hours
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < N and 0 <= new_col < M and grid[new_row][new_col] != '.' and (new_row, new_col) not in visited:
                heappush(pq, (bfs(new_row, new_col), (new_row, new_col)))

    return man_hours

# Read input
T = int(input())
for i in range(1, T + 1):
    man_hours = min_bridge_hours()
    print(f"Case #{i}: {man_hours}")
# Generator time: 23.2548 seconds