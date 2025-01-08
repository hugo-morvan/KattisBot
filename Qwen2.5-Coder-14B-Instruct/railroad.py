def simplify_railroad_map():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        graph = {}
        
        for _ in range(M):
            a = int(data[index]) - 1
            b = int(data[index + 1]) - 1
            c = int(data[index + 2])
            index += 3
            
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            
            graph[a].append((b, c))
            graph[b].append((a, c))
        
        # Identify stations with exactly two connections
        to_remove = set()
        for station in range(N):
            if len(graph[station]) == 2:
                to_remove.add(station)
        
        # Remove such stations and update distances
        new_graph = {}
        for station in range(N):
            if station not in to_remove:
                new_edges = []
                for neighbor, distance in graph[station]:
                    if neighbor not in to_remove:
                        new_edges.append((neighbor + 1, distance))
                if new_edges:
                    new_graph[station + 1] = new_edges
        
        # Collect the simplified map
        K = len(new_graph)
        railroads = []
        for station, edges in new_graph.items():
            for neighbor, distance in edges:
                railroads.append((station, neighbor, distance))
        
        results.append((K, railroads))
    
    # Print results
    for K, railroads in results:
        print(K)
        for a, b, c in railroads:
            print(a, b, c)
        print()

simplify_railroad_map()
# Generator time: 55.4253 seconds