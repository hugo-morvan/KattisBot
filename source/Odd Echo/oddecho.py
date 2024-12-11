# Read the number of lines
N = int(input())

# Initialize an empty list to store the words
words = []

# Read the words from the input
for _ in range(N):
    words.append(input())

# Initialize an empty list to store the echoed words
echoed_words = []

# Iterate over the words and collect the odd-indexed ones
for i in range(0, N, 2):
    echoed_words.append(words[i])

# Print the echoed words
print('\n'.join(echoed_words))