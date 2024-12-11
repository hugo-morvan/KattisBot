import sys

# Read input
S = input()
M = input()

# Split the memo into words
memo_words = M.split()

# Create a set of forbidden words
forbidden_words = set(S)

# Process each word in the memo
processed_memo = []
for word in memo_words:
    if any(char in forbidden_words for char in word):
        # Replace forbidden letters with '*'
        processed_word = ''.join('*' if char in forbidden_words else char for char in word)
    else:
        processed_word = word
    processed_memo.append(processed_word)

# Join the processed words back into a single string
output = ' '.join(processed_memo)

# Print the output
print(output)