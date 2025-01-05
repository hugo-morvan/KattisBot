import sys
from collections import Counter

def hand_rank(hand):
    ranks = sorted([rank for rank, _ in hand])
    suits = sorted([suit for _, suit in hand])
    
    # Check for royal flush
    if ranks == ['A', 'K', 'Q', 'J', 'T'] and suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return 250
    
    # Check for straight flush
    if ranks == list(range(min(ranks), max(ranks) + 1)) and suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return 100
    
    # Check for four of a kind
    if len(Counter(ranks).values()) == 2:
        return payouts[4]
    
    # Check for full house
    if len(Counter(ranks).values()) == 2:
        return payouts[3]
    
    # Check for flush
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return payouts[5]
    
    # Check for straight
    if ranks == list(range(min(ranks), max(ranks) + 1)):
        return payouts[4]
    
    # Check for three of a kind
    if len(Counter(ranks).values()) == 3:
        return payouts[2]
    
    # Check for two pairs
    if len(Counter(ranks).values()) == 3:
        return payouts[1]
    
    # Check for one pair
    if len(Counter(ranks).values()) == 2:
        return payouts[0]
    
    return 0

def expected_reward(payouts, hand):
    n = len(hand)
    total_reward = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            remaining_hand = hand[:i] + hand[j:]
            remaining_deck = list(set(deck) - set(remaining_hand))
            
            for k in range(5 - len(remaining_hand)):
                new_card = remaining_deck.pop()
                new_hand = remaining_hand + [new_card]
                reward = hand_rank(new_hand)
                total_reward += reward
    
    return total_reward / (n * (n + 1) // 2)

# Read input
payouts = list(map(int, input().split()))
n = int(input())
deck = '23456789TJQKA' * 4
hands = []

for _ in range(n):
    hand = tuple(input().split())
    hands.append(hand)

# Calculate and print expected rewards
for hand in hands:
    expected_reward_value = expected_reward(payouts, hand)
    print(f"{expected_reward_value:.6f}")
# Generator time: 25.6612 seconds