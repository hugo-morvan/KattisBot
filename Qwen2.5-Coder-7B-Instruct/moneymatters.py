def can_settle_debts(n, m, balances, friendships):
    from collections import defaultdict
    
    # Create a graph to represent the remaining friendships
    graph = defaultdict(list)
    for x, y in friendships:
        graph[x].append(y)
        graph[y].append(x)
    
    # Function to check if we can settle debts between friends using DFS
    def dfs(node, parent):
        visited[node] = True
        stack.append(node)
        
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
        
        return len(stack) == 0
    
    # Check if we can settle debts between all friends
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            if not dfs(i, -1):
                return "IMPOSSIBLE"
    
    return "POSSIBLE"

# Input parsing
n, m = map(int, input().split())
balances = [int(input()) for _ in range(n)]
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(can_settle_debts(n, m, balances, friendships))
# Generator time: 8.8634 seconds