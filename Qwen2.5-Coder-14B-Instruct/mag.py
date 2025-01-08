from fractions import Fraction
import sys

def find_min_magic_path(n, edges, magic):
    # Build the tree using adjacency list representation
    from collections import defaultdict
    
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Function to perform DFS and calculate the path with minimal magic
    def dfs(node, parent):
        min_magic = Fraction(magic[node - 1], 1)  # Start with the magic of the current node
        
        for neighbor in tree[node]:
            if neighbor != parent:
                neighbor_magic = dfs(neighbor, node)
                combined_magic = (min_magic * Fraction(magic[neighbor - 1], 1)) / Fraction(2, 1)
                min_magic = min(min_magic, combined_magic)
        
        return min_magic
    
    # Start DFS from any node, typically node 1
    min_magic_path = dfs(1, -1)
    
    # Output the result as a completely reduced fraction P/Q
    print(f"{min_magic_path.numerator}/{min_magic_path.denominator}")

# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
magic = list(map(int, input().split()))

# Find and output the path with minimal magic
find_min_magic_path(n, edges, magic)
# Generator time: 38.1102 seconds