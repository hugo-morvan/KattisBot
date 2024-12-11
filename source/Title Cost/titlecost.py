def calculate_transmission_cost(title, cap):
    # Calculate the length of the movie title
    title_length = len(title)
    
    # Determine the cost based on the minimum of the title length and the cap
    cost = min(title_length, cap)
    
    # Return the calculated cost
    return cost

# Read input values
title = input()
cap = float(input())

# Calculate and print the transmission cost
print(calculate_transmission_cost(title, cap))