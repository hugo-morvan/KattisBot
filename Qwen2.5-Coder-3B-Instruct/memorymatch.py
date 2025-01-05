def max_matching_pairs(N, K, turns):
    # Dictionary to track the status of each card (face-up or face-down)
    card_status = {i: 'down' for i in range(1, N + 1)}
    
    # Counter for the number of matching pairs
    matching_pairs = 0
    
    # Process each turn
    for turn in turns:
        C1, C2, P1, P2 = turn
        
        # Check if both cards are already face-up
        if card_status[C1] == 'up' and card_status[C2] == 'up':
            matching_pairs += 1
            card_status[C1] = 'down'
            card_status[C2] = 'down'
        
        # Otherwise, mark both cards as face-up
        else:
            card_status[C1] = 'up'
            card_status[C2] = 'up'
    
    return matching_pairs

# Read input
N = int(input())
K = int(input())
turns = [tuple(map(int, input().split())) + tuple(input().split()) for _ in range(K)]

# Calculate the maximum number of matching pairs
result = max_matching_pairs(N, K, turns)

# Output the result
print(result)
# Generator time: 26.2501 seconds