def find_valid_k(n, m, roads):
    from itertools import combinations

    def has_equal_distribution(tours, k):
        from collections import defaultdict
        road_counts = defaultdict(int)
        
        for tour in tours:
            for i in range(len(tour)):
                if i + 1 == len(tour):
                    road = (tour[i], tour[0])
                else:
                    road = tuple(sorted((tour[i], tour[i + 1])))
                road_counts[road] += 1
        
        counts_per_company = [0] * k
        for count in road_counts.values():
            if count % k != 0:
                return False
        
        return True

    def find_tours(n, m, roads):
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, path, visited):
            if len(path) >= 3 and node == path[0]:
                tours.append(path[:])
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, path + [neighbor], visited):
                        return True
            visited.remove(node)
            return False
        
        tours = []
        for start in range(1, n + 1):
            dfs(start, [start], set())
        return tours

    tours = find_tours(n, m, roads)
    
    valid_ks = []
    for k in range(1, m + 1):
        if has_equal_distribution(tours, k):
            valid_ks.append(k)
    
    print(' '.join(map(str, valid_ks)))

# Input
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Find and output valid k values
find_valid_k(n, m, roads)
# Generator time: 14.3889 seconds