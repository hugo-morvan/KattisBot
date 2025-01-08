from fractions import Fraction
import sys

# Read input
input = sys.stdin.read
data = input().split()

N = int(data[0])
edges = []
for i in range(N-1):
    A = int(data[2*i+1]) - 1
    B = int(data[2*i+2]) - 1
    edges.append((A, B))
magic = [int(data[N+i+1]) for i in range(N)]

# Build the graph
from collections import defaultdict
graph = defaultdict(list)
for A, B in edges:
    graph[A].append(B)
    graph[B].append(A)

# Function to find all paths from node u to leaf and calculate their magic
def find_paths(node, parent, path):
    path.append(magic[node])
    if len(graph[node]) == 1 and node != 0:  # Leaf node
        yield path[:]
    for neighbor in graph[node]:
        if neighbor != parent:
            yield from find_paths(neighbor, node, path)
    path.pop()

# Initialize minimum magic to a large number
min_magic = Fraction(sys.maxsize)

# Iterate over all paths and calculate their magic
for start_node in range(N):
    for path in find_paths(start_node, -1, []):
        current_magic = Fraction(magic[start_node] * magic[start_node], len(path))
        min_magic = min(min_magic, current_magic)

# Output the result as a reduced fraction
print(f"{min_magic.numerator}/{min_magic.denominator}")
# Generator time: 11.1809 seconds