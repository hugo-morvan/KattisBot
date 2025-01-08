from collections import Counter

def evaluate_hand(hand):
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    
    # Convert ranks to numerical values
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    ranks = [rank_values[r] for r in ranks]
    
    rank_count = Counter(ranks)
    suit_count = Counter(suits)
    
    # Check for royal flush
    if len(set(suits)) == 1 and max(ranks) - min(ranks) == 4 and set(ranks) == {10, 11, 12, 13, 14}:
        return 9
    
    # Check for straight flush
    if len(set(suits)) == 1 and (max(ranks) - min(ranks) == 4 or (min(ranks) == 2 and max(ranks) == 14)):
        return 8
    
    # Check for four of a kind
    if any(v == 4 for v in rank_count.values()):
        return 7
    
    # Check for full house
    if any(v == 3 for v in rank_count.values()) and any(v == 2 for v in rank_count.values()):
        return 6
    
    # Check for flush
    if len(set(suits)) == 1:
        return 5
    
    # Check for straight
    ranks.sort()
    if (max(ranks) - min(ranks) == 4 or (min(ranks) == 2 and max(ranks) == 14)):
        return 4
    
    # Check for three of a kind
    if any(v == 3 for v in rank_count.values()):
        return 3
    
    # Check for two pairs
    if list(rank_count.values()).count(2) == 2:
        return 2
    
    # Check for one pair
    if any(v == 2 for v in rank_count.values()):
        return 1
    
    # High card
    return 0

def expected_reward(hand, payouts):
    current_rank = evaluate_hand(hand)
    if current_rank == 9:  # Royal flush
        return payouts[9]
    
    max_expected = 0
    
    for i in range(5):
        for j in range(i + 1, 6):
            new_hand = hand[:i] + hand[j:]
            remaining_ranks = [card[0] for card in hand if card not in new_hand]
            remaining_suits = [card[1] for card in hand if card not in new_hand]
            
            # Calculate the expected reward by replacing cards
            remaining_deck_size = 52 - len(hand)
            expected_value = payouts[current_rank]
            for _ in range(5 - len(new_hand)):
                replacement_card = (remaining_ranks.pop(), remaining_suits.pop())
                new_hand.append(replacement_card)
                new_hand.sort()
                new_rank = evaluate_hand(new_hand)
                expected_value += payouts[new_rank] / remaining_deck_size
                remaining_deck_size -= 1
            
            max_expected = max(max_expected, expected_value)
    
    return max_expected

# Read input
payouts = list(map(int, input().split()))
n = int(input())
hands = [input().split() for _ in range(n)]

# Calculate and print the expected reward for each hand
for hand in hands:
    result = expected_reward(hand, payouts)
    print(f"{result:.6f}")
# Generator time: 109.1987 seconds