def coconut_splat(s, n):
    # Initialize the list of players with True indicating they are still in the game
    players = [True] * n
    
    # Initialize the current player index
    current_player = 0
    
    while len(players) > 1:
        # Determine which player's hand is touched last
        touched_last = -1
        for i in range(n):
            if players[i]:
                # Touch the hand of the player at the current position
                players[i] = False
                touched_last = i
        
        # Apply the action based on the number of syllables
        if s == 10:
            # If the rhyme has 10 syllables, the last player to touch a hand loses
            players[touched_last] = False
        else:
            # If the rhyme has fewer than 10 syllables, the last player to touch a hand loses
            players[touched_last] = False
        
        # Move to the next player
        current_player = (current_player + 1) % n
    
    # Return the index of the remaining player
    return current_player + 1

# Read input
s, n = map(int, input().split())

# Output the result
print(coconut_splat(s, n))