def get_payout(hand):
    """Given the payout structure, determine the expected reward for one hand"""
    # hand is a list of 5 cards, each with format "Xs", X is rank and s is suit
    # rank is from 2 to Ace (10 points)
    # suit is c(lubs), d(iamonds), h(earts), s(pades)
    # convert the hand into a dictionary of ranks
    hand_dict = {}
    for card in hand:
        rank = card[0]
        if rank == 'T':
            rank = 10
        elif rank == 'J':
            rank = 11
        elif rank == 'Q':
            rank = 12
        elif rank == 'K':
            rank = 13
        elif rank == 'A':
            rank = 14
        suit = card[1]
        if rank in hand_dict:
            hand_dict[rank].append(suit)
        else:
            hand_dict[rank] = [suit]
    # determine the type of hand and return the payout
    hand_type = None
    for key in hand_dict:
        if len(hand_dict[key]) == 5:
            if key in range(2, 10):
                hand_type = "one pair"
            else:
                hand_type = "straight"
    if hand_type is None:
        for key in hand_dict:
            if len(hand_dict[key]) == 2:
                if key in range(2, 10):
                    hand_type = "two pairs"
                else:
                    hand_type = "three of a kind"
        if hand_type is None:
            for key in hand_dict:
                if len(hand_dict[key]) == 3:
                    hand_type = "full house"
            if hand_type is None:
                for key in hand_dict:
                    if len(hand_dict[key]) == 4:
                        hand_type = "four of a kind"
                if hand_type is None:
                    for key in hand_dict:
                        if len(hand_dict[key]) == 5:
                            if key in range(2, 10):
                                hand_type = "straight flush"
                            else:
                                hand_type = "royal flush"
    return payouts[hand_type]

payouts = {'one pair':1,'two pairs':2,'three of a kind':3,'straight':4,
           'flush':5,'full house':10,'four of a kind':25,
           'straight flush':100,'royal flush':250}

n = int(input())
for _ in range(n):
    hand = list(input().split())
    print("%.6f" % get_payout(hand))
# Generator time: 18.1989 seconds