import sys
input = sys.stdin.read
data = input().split()

c = int(data[0])
t = int(data[1])

edges = []
index = 2
for _ in range(t):
    a = int(data[index])
    b = int(data[index + 1])
    edges.append((a, b))
    index += 2

# Step 1: Build the graph
from collections import defaultdict
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# Step 2: Find an Eulerian path (if possible) or use Hierholzer's algorithm to find an Eulerian circuit
def find_eulerian_path(graph):
    odd_degree_nodes = [node for node, neighbors in graph.items() if len(neighbors) % 2 == 1]
    
    if not odd_degree_nodes:
        start_node = next(iter(graph))
    elif len(odd_degree_nodes) == 2:
        start_node = odd_degree_nodes[0]
    else:
        return None
    
    path = []
    stack = [start_node]

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())

    return path[::-1]

# Step 3: Divide the remaining chambers
def divide_chambers(c, initial_path):
    remaining_chambers = set(range(1, c + 1)) - set(initial_path)
    
    s = len(remaining_chambers) // 2
    
    # Randomly split the remaining chambers
    kid1 = list(remaining_chambers)[:s]
    kid2 = list(remaining_chambers)[s:]
    
    return kid1, kid2

# Step 4: Output the result
initial_path = find_eulerian_path(graph)
if not initial_path:
    raise ValueError("No valid Eulerian path found")

p = len(initial_path)
s = (c - p) // 2

print(p, s)
print(*initial_path)
kid1, kid2 = divide_chambers(c, initial_path)
print(*kid1)
print(*kid2)
# Generator time: 61.7014 seconds