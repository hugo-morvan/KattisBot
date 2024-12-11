from collections import Counter

def hand_strength(hand):
    # Count the frequency of each rank in the hand
    rank_counts = Counter(card[0] for card in hand)
    
    # Find the maximum number of cards with the same rank
    max_strength = max(rank_counts.values(), default=0)
    
    return max_strength

# Read input
input_hand = input().split()

# Compute and print the hand strength
print(hand_strength(input_hand))