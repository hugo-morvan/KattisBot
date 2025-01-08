import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2
    
    colors = list(map(int, data[idx:idx + N]))
    idx += N
    
    parents = list(map(int, data[idx:idx + N - 1]))
    idx += N - 1
    
    tree = defaultdict(list)
    for i in range(1, N):
        tree[parents[i - 1]].append(i)
    
    color_count = [0] * 101
    magic_count = [0] * N
    
    def dfs(node):
        nonlocal magic_count, color_count
        
        original_color = colors[node]
        color_count[original_color] += 1
        if color_count[original_color] % 2 == 1:
            magic_count[node] += 1
        else:
            magic_count[node] -= 1
        
        for child in tree[node]:
            dfs(child)
        
        magic_count[node] = sum(magic_count[child] for child in tree[node])
        if color_count[original_color] % 2 == 1:
            magic_count[node] += 1
        else:
            magic_count[node] -= 1
        
        color_count[original_color] -= 1
    
    dfs(0)
    
    results = []
    for i in range(Q):
        K = int(data[idx])
        X = int(data[idx + 1]) - 1
        idx += 2
        
        if K == 0:
            results.append(magic_count[X])
        else:
            original_color = colors[X]
            new_color = K
            
            color_count[original_color] -= 1
            if color_count[original_color] % 2 == 0:
                magic_count[X] -= 1
            
            color_count[new_color] += 1
            if color_count[new_color] % 2 == 1:
                magic_count[X] += 1
            
            colors[X] = new_color
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 62.7798 seconds