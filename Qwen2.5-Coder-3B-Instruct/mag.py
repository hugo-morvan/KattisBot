from math import gcd

def dfs(node, parent, magic, path_magic, path_length):
    # Update the path magic and length
    path_magic *= magic
    path_length += 1
    
    # Calculate the current magic value for the path
    current_magic = path_magic / path_length
    
    # Check if this is the minimal magic found so far
    global min_magic, min_path
    if current_magic < min_magic:
        min_magic = current_magic
        min_path = path_magic, path_length
    
    # Explore children
    for child in graph[node]:
        if child != parent:
            dfs(child, node, magic, path_magic, path_length)

def find_min_magic_path(N, edges, magic_values):
    global min_magic, min_path
    min_magic = float('inf')
    min_path = None
    
    # Build the graph
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform DFS from each node
    for node in range(1, N + 1):
        dfs(node, 0, magic_values[node], 1, 1)
    
    # Convert the minimal magic to a reduced fraction
    numerator, denominator = min_path
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    
    # Output the result
    print(f"{numerator}/{denominator}")

# Read input
N = int(input())
edges = []
magic_values = []

for _ in range(N - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

for _ in range(N):
    magic_values.append(int(input()))

# Find and print the minimal magic path
find_min_magic_path(N, edges, magic_values)
# Generator time: 30.3452 seconds