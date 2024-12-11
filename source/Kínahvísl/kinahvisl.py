def min_people_for_whispering_game(initial_word, final_word):
    # Find the index of the differing letter
    for i in range(len(initial_word)):
        if initial_word[i] != final_word[i]:
            # The differing letter affects at most two people
            return 3
    
    # If no differing letter is found, it means the words are identical
    return 1

# Read input
initial_word = input()
final_word = input()

# Calculate and print the minimum number of people
print(min_people_for_whispering_game(initial_word, final_word))