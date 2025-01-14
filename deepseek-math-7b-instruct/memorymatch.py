 def max_pairs(N, K):
    # Initialize a set to store all card positions 
    cards = set()
    
    for _ in range(K):
        _, C2, P1, P2 = input().split(" ")
        
        if P1 == P2:
            continue
            
        # Add both card positions to the set 
        cards.add(C1)
        cards.add(C2)
    
    return len(cards) // 2
# Generator time: 5.3070 seconds