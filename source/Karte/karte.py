from collections import Counter

def check_poker_deck(deck):
    # Define the suits
    suits = ['P', 'K', 'H', 'T']
    
    # Count the occurrences of each card label
    card_counts = Counter(deck)
    
    # Initialize the list to store the number of missing cards for each suit
    missing_cards = [0] * 4
    
    # Iterate over each suit
    for i, suit in enumerate(suits):
        # Calculate the expected number of cards for this suit
        expected_count = 13
        # Subtract the count of the current suit from the expected count
        missing_cards[i] = expected_count - card_counts.get(suit, 0)
    
    # Check if there are any duplicate cards
    if len(card_counts) != len(deck):
        return "GRESKA"
    
    # Print the result as a space-separated string
    print(" ".join(map(str, missing_cards)))

# Read the input string
deck_labels = input()

# Call the function to check the deck
check_poker_deck(deck_labels)