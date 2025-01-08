from collections import Counter

def find_fake_pair():
    n = int(input())
    pairs = []
    
    for _ in range(n // 2 + 1):
        a, b = map(int, input().split())
        pairs.append((min(a, b), max(a, b)))
    
    # Count occurrences of each pair
    count = Counter(pairs)
    
    # Find the pair that appears only once
    for pair in count:
        if count[pair] == 1:
            print(pair[0], pair[1])
            return

find_fake_pair()
# Generator time: 5.3178 seconds