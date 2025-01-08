def dfs(node, visited, graph, balance):
    stack = [node]
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor] and balance[neighbor] != 0:
                visited[neighbor] = True
                stack.append(neighbor)

def is_possible_to_balance(n, m, balances, friendships):
    graph = [[] for _ in range(n)]
    
    # Build the graph based on friendships
    for x, y in friendships:
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [False] * n
    total_balance = sum(balances)
    
    if total_balance != 0:
        return "IMPOSSIBLE"
    
    # Check connected components and their balances
    for i in range(n):
        if not visited[i] and balances[i] != 0:
            dfs(i, visited, graph, balances)
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

# Read input
n, m = map(int, input().split())
balances = [int(input()) for _ in range(n)]
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(is_possible_to_balance(n, m, balances, friendships))
# Generator time: 36.8996 seconds