def choose_friend(n, friends):
    mantra = "Úllen dúllen doff kikke lane koff koffe lane bikke bane úllen dúllen doff"
    words = mantra.split()
    
    # Find the position of the first word in the mantra
    start_word_index = words.index(words[0])
    
    # Determine the starting index for the loop
    start_index = (start_word_index + n) % n
    
    # Print the friend at the starting index
    print(friends[start_index])

# Read input
n = int(input())
friends = input().split()

# Choose the friend
choose_friend(n, friends)