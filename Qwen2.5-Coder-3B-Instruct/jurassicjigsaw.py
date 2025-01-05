import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])

samples = [data[i] for i in range(2, 2 + n)]

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def build_tree(samples):
    if len(samples) == 1:
        return 0, []
    
    min_unlikeliness = float('inf')
    best_edges = []
    
    for i in range(len(samples)):
        for j in range(i + 1, len(samples)):
            distance = hamming_distance(samples[i], samples[j])
            current_unlikeliness = distance + build_tree([samples[i]])[0] + build_tree([samples[j]])[0]
            
            if current_unlikeliness < min_unlikeliness:
                min_unlikeliness = current_unlikeliness
                best_edges = [(i, j)]
    
    return min_unlikeliness, best_edges

min_unlikeliness, edges = build_tree(samples)

print(min_unlikeliness)
for edge in edges:
    print(edge[0], edge[1])
# Generator time: 10.9998 seconds