from collections import defaultdict, deque

def count_magical_colors(N, Q, colors, parent_edges):
    # Build the tree structure
    tree = defaultdict(list)
    for i in range(1, N):
        u, v = i + 1, parent_edges[i]
        tree[u].append(v)
        tree[v].append(u)

    # Initialize color counts for each node and its subtree
    color_counts = [defaultdict(int) for _ in range(N + 1)]
    
    def dfs(node, parent):
        current_color_count = defaultdict(int)
        for neighbor in tree[node]:
            if neighbor != parent:
                child_color_count = dfs(neighbor, node)
                for color, count in child_color_count.items():
                    current_color_count[color] += count
        current_color_count[colors[node - 1]] += 1
        color_counts[node] = current_color_count
        return current_color_count
    
    # Perform DFS to get initial color counts
    dfs(1, -1)
    
    # Initialize answer for each query
    answers = []
    
    def is_magical(count):
        return sum(1 for count in count.values() if count % 2 == 1) > 0
    
    for K, X in queries:
        if K == 0:
            magical_count = sum(is_magical(color_counts[X]) for X in range(1, N + 1))
            answers.append(magical_count)
        else:
            color_counts[X][colors[X - 1]] -= 1
            colors[X - 1] = K
            color_counts[X][K] += 1
    
    return answers

# Read input
N, Q = map(int, input().split())
colors = list(map(int, input().split()))
parent_edges = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Process queries and print results
results = count_magical_colors(N, Q, colors, parent_edges)
for result in results:
    print(result)
# Generator time: 14.6704 seconds