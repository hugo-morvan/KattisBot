import sys
from collections import defaultdict, deque

def find_path_and_partition(c, t, tunnels):
    # Step 1: Find an Eulerian path in the graph
    graph = defaultdict(list)
    degree = [0] * (c + 1)
    
    for a, b in tunnels:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1
    
    # Find starting and ending points of the Eulerian path
    start = None
    end = None
    for i in range(1, c + 1):
        if degree[i] % 2 == 1:
            if not start:
                start = i
            else:
                end = i
    
    # If no odd-degree vertices, any vertex can be the start
    if start is None:
        start = 1
    
    # Step 2: Find an Eulerian path starting from 'start'
    stack = [start]
    path = []
    
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
    
    # Reverse the path to get the correct order
    path.reverse()
    
    # Step 3: Partition the remaining chambers between two kids
    n = len(path)
    s = n // 2
    kid1 = path[:s]
    kid2 = path[s:]
    
    # Output the results
    p = n
    print(p, s)
    print(' '.join(map(str, path)))
    print(' '.join(map(str, kid1)))
    print(' '.join(map(str, kid2)))

# Read input
c, t = map(int, input().split())
tunnels = [tuple(map(int, input().split())) for _ in range(t)]

# Solve and output the result
find_path_and_partition(c, t, tunnels)
# Generator time: 12.6587 seconds