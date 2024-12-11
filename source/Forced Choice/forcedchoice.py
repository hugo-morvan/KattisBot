# Read input
N, P, S = map(int, input().split())
cards = list(range(1, N + 1))
steps = []

for _ in range(S):
    m, *chosen_cards = map(int, input().split())
    steps.append((m, chosen_cards))

# Process each step
for m, chosen_cards in steps:
    # Check the parity of the number of chosen cards
    if m % 2 == 0:
        # If even, remove the chosen cards
        for card in chosen_cards:
            if card in cards:
                cards.remove(card)
    else:
        # If odd, keep the chosen cards
        for card in chosen_cards:
            if card in cards:
                cards.append(card)

# Print the result for each step
for m, _ in steps:
    if m % 2 == 0:
        print("REMOVE")
    else:
        print("KEEP")