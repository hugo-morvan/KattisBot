import heapq

def calculate_unlikeliness(dna1, dna2):
    return sum(1 for a, b in zip(dna1, dna2) if a != b)

def find_minimal_unlikeliness(n, k, samples):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            unlikeliness = calculate_unlikeliness(samples[i], samples[j])
            heapq.heappush(edges, (unlikeliness, i, j))
    
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    total_unlikeliness = 0
    min_edges = []
    while edges and len(min_edges) < n - 1:
        unlikeliness, u, v = heapq.heappop(edges)
        if find(u) != find(v):
            union(u, v)
            total_unlikeliness += unlikeliness
            min_edges.append((u, v))
    
    print(total_unlikeliness)
    for edge in min_edges:
        print(edge[0], edge[1])

# Input reading
n, k = map(int, input().split())
samples = [input() for _ in range(n)]

# Output result
find_minimal_unlikeliness(n, k, samples)
# Generator time: 13.1730 seconds