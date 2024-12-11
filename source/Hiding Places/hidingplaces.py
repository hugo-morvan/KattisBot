def knight_moves(x, y):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    return [(x + dx, y + dy) for dx, dy in directions]

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs(start_x, start_y, n):
    queue = [(start_x, start_y, 0)]
    visited = set()
    visited.add((start_x, start_y))
    
    while queue:
        x, y, steps = queue.pop(0)
        
        if steps > 0:
            yield steps, (x, y)
        
        for nx, ny in knight_moves(x, y):
            if is_valid(nx, ny, n) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

def find_hiding_places(start_x, start_y, n):
    max_steps = 0
    hiding_places = []
    
    for steps, (x, y) in bfs(start_x, start_y, n):
        if steps > max_steps:
            max_steps = steps
            hiding_places = [(x, y)]
        elif steps == max_steps:
            hiding_places.append((x, y))
    
    return max_steps, sorted(hiding_places)

def main():
    n = int(input())
    results = []
    
    for _ in range(n):
        start = input().split()
        start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
        n = 8
        max_steps, hiding_places = find_hiding_places(start_x, start_y, n)
        results.append(f"{max_steps} {' '.join([f'{chr(ord('a') + x)}{y + 1}' for x, y in hiding_places])}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()