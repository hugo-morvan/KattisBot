from collections import defaultdict, deque

def bfs(graph, start):
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        current, debt = queue.popleft()
        
        # Add the debt of the current friend to the total debt
        total_debt += debt
        
        # Explore all friends of the current friend
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, debt + graph[current][neighbor]))
    
    return total_debt

def main():
    n, m = map(int, input().split())
    
    # Initialize the graph
    graph = defaultdict(dict)
    
    # Read the balances of each friend
    balances = list(map(int, input().split()))
    
    # Read the friendships
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = balances[y]
        graph[y][x] = -balances[x]
    
    total_debt = 0
    
    # Check if it's possible to settle the debts
    for i in range(n):
        total_debt += bfs(graph, i)
    
    if total_debt == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
# Generator time: 28.2290 seconds