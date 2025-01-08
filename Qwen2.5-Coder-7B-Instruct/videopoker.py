from itertools import combinations

# Define the ranks in order
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Define the suits
suits = ['c', 'd', 'h', 's']

# Function to convert a card string to its rank index
def card_to_rank(card):
    return ranks.index(card[:-1])

# Function to get the number of each rank in a hand
def count_ranks(hand):
    count = [0] * 13
    for card in hand:
        count[card_to_rank(card)] += 1
    return count

# Function to determine if a hand is a straight flush or royal flush
def is_straight_flush_or_royal_flush(hand):
    ranks_in_hand = sorted([card_to_rank(card) for card in hand])
    suits_in_hand = [card[-1] for card in hand]
    
    # Check for straight flush and royal flush
    if len(set(suits_in_hand)) == 1:
        if ranks_in_hand == [0, 1, 2, 3, 12]:
            return 'royal_flush'
        elif ranks_in_hand[4] - ranks_in_hand[0] == 4:
            return 'straight_flush'
    
    return None

# Function to determine the best hand from a list of hands
def get_best_hand(hands):
    best_rank = None
    best_payout = 0
    
    for hand in hands:
        rank_counts = count_ranks(hand)
        
        # Check for royal flush and straight flush
        if (best_rank is None or best_rank == 'royal_flush') and 'royal_flush' in [is_straight_flush_or_royal_flush([hand[i] for i in indices]) for indices in combinations(range(5), 5)]:
            best_rank = 'royal_flush'
            best_payout = 250
        elif (best_rank is None or best_rank == 'straight_flush') and 'straight_flush' in [is_straight_flush_or_royal_flush([hand[i] for i in indices]) for indices in combinations(range(5), 5)]:
            best_rank = 'straight_flush'
            best_payout = 100
        
        # Check for other hands
        if best_rank is None:
            for rank in range(2, 13):
                if rank_counts[rank] >= 4:
                    best_rank = 'four_of_a_kind'
                    best_payout = 25
                elif rank_counts[rank] == 3:
                    if any(rank_counts[i] == 2 for i in range(13) if i != rank):
                        best_rank = 'full_house'
                        best_payout = 10
                    else:
                        best_rank = 'three_of_a_kind'
                        best_payout = 3
                elif rank_counts[rank] == 2:
                    pairs_count = sum(1 for i in range(13) if rank_counts[i] == 2)
                    if pairs_count >= 2:
                        best_rank = 'two_pairs'
                        best_payout = 2
                    else:
                        best_rank = 'one_pair'
                        best_payout = 1
        
        # If we have a straight, flush, or other hand with the same number of cards as the current best, keep it
        if (best_rank is None or best_rank == 'straight' and len([i for i in range(5) if rank_counts[card_to_rank(hand[i])] > 0]) <= len([i for i in range(5) if rank_counts[i] > 0])) and 'straight' in [is_straight_flush_or_royal_flush([hand[i] for i in indices]) for indices in combinations(range(5), 5)]:
            best_rank = 'straight'
            best_payout = 4
        elif (best_rank is None or best_rank == 'flush' and len([i for i in range(5) if rank_counts[card_to_rank(hand[i])] > 0]) <= len([i for i in range(5) if rank_counts[i] > 0])) and 'flush' in [is_straight_flush_or_royal_flush([hand[i] for i in indices]) for indices in combinations(range(5), 5)]:
            best_rank = 'flush'
            best_payout = 5
    
    return best_rank, best_payout

# Read input
payout_structure = list(map(int, input().split()))
n = int(input())
starting_hands = [input().split() for _ in range(n)]

# Calculate and print the expected reward for each hand
for hand in starting_hands:
    best_hand, payout = get_best_hand(hand)
    print(payout)
# Generator time: 26.7723 seconds