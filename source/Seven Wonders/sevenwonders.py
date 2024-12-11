# Read the input string
input_string = input()

# Initialize counters for each type of card
tablet_count = 0
compass_count = 0
gear_count = 0

# Count the occurrences of each type of card
for card in input_string:
    if card == 'T':
        tablet_count += 1
    elif card == 'C':
        compass_count += 1
    elif card == 'G':
        gear_count += 1

# Calculate the points from individual cards
individual_points = tablet_count**2 + compass_count**2 + gear_count**2

# Calculate the points from sets of three different cards
sets_of_three_points = (min(tablet_count, compass_count, gear_count) // 3) * 7

# Total points
total_points = individual_points + sets_of_three_points

# Output the total points
print(total_points)