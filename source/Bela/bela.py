def calculate_points(N, dominant_suit):
    # Define the values of cards based on their number and suit
    card_values = {
        'A': 11 if dominant_suit == 'S' else 11,
        'K': 4 if dominant_suit == 'S' else 4,
        'Q': 3 if dominant_suit == 'S' else 3,
        'J': 20 if dominant_suit == 'S' else 2,
        'T': 10 if dominant_suit == 'S' else 10,
        '9': 14 if dominant_suit == 'S' else 0,
        '8': 0 if dominant_suit == 'S' else 0,
        '7': 0 if dominant_suit == 'S' else 0
    }
    
    # Read the input data
    hands = []
    for _ in range(4 * N):
        card, suit = input().split()
        hands.append((card, suit))
    
    # Calculate the total points
    total_points = 0
    for card, suit in hands:
        total_points += card_values[card]
    
    # Output the total points
    print(total_points)

# Read the input values
N, dominant_suit = input().split()
calculate_points(int(N), dominant_suit)