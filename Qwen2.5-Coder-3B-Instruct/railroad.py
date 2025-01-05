def read_input():
    T = int(input())
    test_cases = []
    for _ in range(T):
        input()
        N, M = map(int, input().split())
        graph = {i: [] for i in range(1, N + 1)}
        
        for _ in range(M):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))
        
        test_cases.append((N, M, graph))
    return test_cases

def simplify_map(N, M, graph):
    # Step 3: Identify stations with two connections
    stations_with_two_connections = set()
    for station in graph:
        if len(graph[station]) == 2:
            stations_with_two_connections.add(station)
    
    # Step 4: Remove the stations
    for station in stations_with_two_connections:
        del graph[station]
        for neighbor, distance in graph.items():
            if station in distance:
                graph[neighbor].remove((station, distance[station]))
    
    # Step 5: Output the simplified map
    K = len(graph)
    print(K)
    for station, neighbors in graph.items():
        for neighbor, distance in neighbors:
            print(station, neighbor, distance)

def main():
    test_cases = read_input()
    for N, M, graph in test_cases:
        simplify_map(N, M, graph)
        print()

if __name__ == "__main__":
    main()
# Generator time: 22.4766 seconds