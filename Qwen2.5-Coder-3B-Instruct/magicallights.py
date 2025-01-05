def dfs(node, parent, color):
    global colors, magical_colors
    if color not in magical_colors:
        magical_colors.add(color)
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, colors[neighbor])

def count_magical_colors(node, parent, color):
    global colors, magical_colors
    if color not in magical_colors:
        magical_colors.add(color)
    for neighbor in graph[node]:
        if neighbor != parent:
            count_magical_colors(neighbor, node, colors[neighbor])

def solve():
    N, Q = map(int, input().split())
    colors = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    for _ in range(Q):
        K, X = map(int, input().split())
        if K == 0:
            magical_colors = set()
            dfs(X - 1, -1, colors[X - 1])
            print(len(magical_colors))
        else:
            colors[X - 1] = K

solve()
# Generator time: 15.3240 seconds