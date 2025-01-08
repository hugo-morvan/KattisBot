import itertools

def calculate_likeliness(dna1, dna2):
    return sum(1 for a, b in zip(dna1, dna2) if a != b)

def find_minimal_unlikeliness_tree(n, k, samples):
    # Calculate the distance matrix
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_likeliness(samples[i], samples[j])
            distances[i][j] = dist
            distances[j][i] = dist

    # Use a simple heuristic to find a good tree (e.g., nearest neighbor)
    edges = []
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        for j in range(n):
            if not used[j]:
                min_dist = float('inf')
                next_node = -1
                for k in range(n):
                    if not used[k] and distances[i][k] < min_dist:
                        min_dist = distances[i][k]
                        next_node = k
                edges.append((i, next_node))
                used[next_node] = True

    # Calculate the total unlikeliness of the tree
    total_unlikeliness = sum(distances[u][v] for u, v in edges)

    return total_unlikeliness, edges

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    samples = data[2:2 + n]
    
    min_unlikeliness, edges = find_minimal_unlikeliness_tree(n, k, samples)
    
    print(min_unlikeliness)
    for u, v in edges:
        print(u, v)

if __name__ == "__main__":
    main()
# Generator time: 51.7368 seconds