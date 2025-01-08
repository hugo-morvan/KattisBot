def simplify_railroad_map():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    results = []
    
    def get_ints():
        nonlocal index
        ints = []
        while index < len(data) and data[index].isdigit():
            ints.append(int(data[index]))
            index += 1
        return ints
    
    for _ in range(get_ints()[0]):
        N, M = get_ints()
        edges = [set() for _ in range(N + 1)]
        degree = [0] * (N + 1)
        
        for _ in range(M):
            a, b, c = get_ints()
            edges[a].add((b, c))
            edges[b].add((a, c))
            degree[a] += 1
            degree[b] += 1
        
        simplified_edges = set()
        visited = [False] * (N + 1)
        
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor, length in edges[node]:
                simplified_edges.add((min(node, neighbor), max(node, neighbor), length))
                dfs(neighbor)
        
        for i in range(1, N + 1):
            if degree[i] != 2:
                dfs(i)
        
        K = len(simplified_edges)
        sorted_edges = sorted(list(simplified_edges))
        
        results.append(f"{K}\n{'\n'.join(f'{a} {b} {c}' for a, b, c in sorted_edges)}")
    
    print('\n\n'.join(results))

simplify_railroad_map()
# Generator time: 10.6439 seconds