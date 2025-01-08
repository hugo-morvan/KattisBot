def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    
    index = 2
    cards = [None] * (N + 1)
    matched = set()
    
    for _ in range(K):
        C1 = int(data[index])
        P1 = data[index + 2]
        C2 = int(data[index + 3])
        P2 = data[index + 4]
        
        if P1 == P2:
            matched.add(C1)
            matched.add(C2)
        
        index += 5
    
    S = len(matched) // 2
    print(S)

if __name__ == "__main__":
    main()
# Generator time: 23.6581 seconds