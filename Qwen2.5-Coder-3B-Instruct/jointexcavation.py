from collections import defaultdict, deque

def find_path_and_divide(chambers, tunnels):
    # Build the graph
    graph = defaultdict(list)
    for a, b in tunnels:
        graph[a].append(b)
        graph[b].append(a)

    # Find the cycle
    def dfs(node, parent, visited):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node, visited):
                    return True
            elif neighbor != parent:
                return True
        return False

    visited = [False] * (chambers + 1)
    cycle_start = None
    for i in range(1, chambers + 1):
        if not visited[i]:
            if dfs(i, None, visited):
                cycle_start = i
                break

    if cycle_start is None:
        print("0 0")
        return

    # Find the path in the cycle
    path = []
    current = cycle_start
    visited = [False] * (chambers + 1)
    while not visited[current]:
        visited[current] = True
        path.append(current)
        current = graph[current][0]

    # Divide the remaining chambers
    num_chambers = len(path)
    half = num_chambers // 2
    child1 = path[:half]
    child2 = path[half:]

    # Output the results
    print(num_chambers, half)
    print(' '.join(map(str, path)))
    print(' '.join(map(str, child1)))
    print(' '.join(map(str, child2)))

# Read input
c, t = map(int, input().split())
tunnels = [tuple(map(int, input().split())) for _ in range(t)]

# Process the input
find_path_and_divide(c, tunnels)
# Generator time: 18.6967 seconds