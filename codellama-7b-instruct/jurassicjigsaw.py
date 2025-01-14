import sys

def get_edges(sample):
    edges = set()
    for i in range(len(sample) - 1):
        for j in range(i + 1, len(sample)):
            if sample[i] != sample[j]:
                edges.add((i, j))
    return edges

def get_tree(edges):
    tree = []
    while len(edges) > 0:
        min_edge = None
        for edge in edges:
            if min_edge is None or edge[2] < min_edge[2]:
                min_edge = edge
        tree.append(min_edge)
        edges.remove(min_edge)
    return tree

def get_weight(tree):
    weight = 0
    for edge in tree:
        weight += edge[2]
    return weight

n, k = map(int, input().split())
samples = []
for _ in range(n):
    samples.append(input())
min_weight = float('inf')
for sample in samples:
    edges = get_edges(sample)
    tree = get_tree(edges)
    weight = get_weight(tree)
    if min_weight > weight:
        min_weight = weight
        best_tree = tree
print(min_weight)
for edge in best_tree:
    print(edge[0], edge[1])
# Generator time: 9.4360 seconds