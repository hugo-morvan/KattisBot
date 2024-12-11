from collections import deque

def find_path_to_ground(tree):
    # Read the input
    K = int(input())
    graph = {}
    
    while True:
        line = input()
        if line == '-1':
            break
        parts = list(map(int, line.split()))
        branch = parts[0]
        children = parts[1:]
        
        if branch not in graph:
            graph[branch] = []
        graph[branch].extend(children)
    
    # Initialize BFS
    queue = deque([(K, [K])])
    visited = set([K])
    
    while queue:
        current_branch, path = queue.popleft()
        
        # Check if we have reached the root
        if current_branch == 1:
            return ' '.join(map(str, path))
        
        for child in graph[current_branch]:
            if child not in visited:
                visited.add(child)
                queue.append((child, path + [child]))

# Read the input and find the path
path = find_path_to_ground()
print(path)