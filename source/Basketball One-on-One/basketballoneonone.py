def determine_winner(record):
    alice_points = 0
    barbara_points = 0
    
    for i in range(0, len(record), 2):
        if record[i] == 'A':
            alice_points += int(record[i+1])
        else:
            barbara_points += int(record[i+1])
    
    if alice_points > barbara_points:
        return 'A'
    elif barbara_points > alice_points:
        return 'B'
    else:
        return 'A'  # In case of a tie, Alice wins according to the rules

# Read input
record = input()

# Determine and print the winner
winner = determine_winner(record)
print(winner)