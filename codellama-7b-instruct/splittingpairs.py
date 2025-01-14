
    import sys
    
    def nim(n):
        return n % 2 == 1
    
    t = int(input())
    
    for i in range(t):
        piles = list(map(int, input().split()))
        max_piles = max(piles)
        
        if nim(max_piles - 2) and sum(piles) % 2 == 1:
            print("Alice")
        else:
            print("Bob")
            
    sys.exit()

# Generator time: 4.9430 seconds