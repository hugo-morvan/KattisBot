import sys
from collections import deque, defaultdict
n, q = map(int, input().split())
nodes = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for i in range(1, n):
    edges[i - 1].append(nodes[i])

def dfs(cur, par=0):
    global nodes
    if par:
        nodes[par] = cur
    for child in edges[cur]:
        dfs(child, cur)

dfs(0)

colors = [[] for _ in range(101)]
for node in nodes:
    colors[nodes[node]].append(node)

def count_magical(subtree):
    if not subtree:
        return 0
    count = 1 if len(subtree) % 2 == 1 else 0
    for child in subtree:
        count += count_magical(colors[child])
    return count

answers = []
for _ in range(q):
    k, x = map(int, input().split())
    if k:
        colors[x] = [k]
    else:
        subtree = colors[x]
        answers.append(count_magical(subtree))

for answer in answers:
    print(answer)
# Generator time: 9.5492 seconds