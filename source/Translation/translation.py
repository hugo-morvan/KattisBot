import sys

# Read input
N = int(input())
swedish_sentence = input()
M = int(input())
dictionary = {}

# Populate the dictionary
for _ in range(M):
    swedish, english = input().split()
    dictionary[swedish] = english

# Translate the sentence
translated_sentence = ' '.join(dictionary[word] for word in swedish_sentence.split())

# Print the result
print(translated_sentence)