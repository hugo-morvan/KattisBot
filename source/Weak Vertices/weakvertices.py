def find_weak_vertices(n):
    if n == -1:
        return []

    # Read adjacency matrix
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))

    # Find all triangles
    triangles = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if adj_matrix[i][j] and adj_matrix[j][k] and adj_matrix[k][i]:
                    triangles.append((i, j, k))

    # Find weak vertices
    weak_vertices = set(range(n))
    for triangle in triangles:
        for vertex in triangle:
            weak_vertices.remove(vertex)

    # Sort weak vertices
    weak_vertices = sorted(weak_vertices)

    return weak_vertices

# Read input
while True:
    n = int(input())
    if n == -1:
        break
    weak_vertices = find_weak_vertices(n)
    print(' '.join(map(str, weak_vertices)))