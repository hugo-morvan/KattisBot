# Read input values
G, S, C = map(int, input().split())

# Calculate total buying power
total_power = G * 6 + S * 3 + C * 1

# Determine best victory card
if total_power >= 8:
    best_victory_card = "Province"
elif total_power >= 5:
    best_victory_card = "Duchy"
elif total_power >= 2:
    best_victory_card = "Estate"
else:
    best_victory_card = ""

# Determine best treasure card
if total_power >= 6:
    best_treasure_card = "Gold"
elif total_power >= 3:
    best_treasure_card = "Silver"
else:
    best_treasure_card = "Copper"

# Output the result
print(best_victory_card + " or " + best_treasure_card)