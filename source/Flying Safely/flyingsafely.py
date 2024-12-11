import sys
from collections import defaultdict

def find_min_pilots(n, m, flights):
    # Build the graph
    graph = defaultdict(list)
    for a, b in flights:
        graph[a].append(b)
        graph[b].append(a)

    # Initialize the visited set and the result list
    visited = set()
    result = []

    # Depth-first search to find a spanning tree
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    # Start DFS from any node (we can choose any node since the graph is connected)
    dfs(1)

    # The number of nodes in the result list is the number of pilots needed
    return len(result)

# Read input
input = sys.stdin.read
data = input().split()

# Parse the number of test cases
num_test_cases = int(data[0])
data = data[1:]

# Process each test case
for i in range(num_test_cases):
    n, m = map(int, data[:2])
    data = data[2:]
    
    # Parse the flights
    flights = []
    for _ in range(m):
        a, b = map(int, data[:2])
        flights.append((a, b))
        data = data[2:]
    
    # Find the minimum number of pilots
    min_pilots = find_min_pilots(n, m, flights)
    
    # Output the result
    print(min_pilots)