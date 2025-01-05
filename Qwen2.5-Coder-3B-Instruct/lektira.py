def reverse_word(word):
    return word[::-1]

def rearrange_words(word):
    # Split the word into three parts
    if len(word) < 3:
        return word
    mid = len(word) // 2
    left = word[:mid]
    middle = word[mid]
    right = word[mid+1:]
    
    # Reverse each part
    reversed_left = reverse_word(left)
    reversed_middle = reverse_word(middle)
    reversed_right = reverse_word(right)
    
    # Rearrange the parts
    rearranged_word = reversed_right + reversed_middle + reversed_left
    return rearranged_word

def find_lexicographically_smallest_word(word):
    smallest_word = word
    for i in range(1, len(word)):
        for j in range(i+1, len(word)):
            # Split the word into three parts
            left = word[:i]
            middle = word[i:j]
            right = word[j:]
            
            # Reverse each part
            reversed_left = reverse_word(left)
            reversed_middle = reverse_word(middle)
            reversed_right = reverse_word(right)
            
            # Rearrange the parts
            rearranged_word = reversed_right + reversed_middle + reversed_left
            
            # Update the smallest word if this one is smaller
            if rearranged_word < smallest_word:
                smallest_word = rearranged_word
    
    return smallest_word

# Read input
word = input()

# Find the lexicographically smallest word
result = find_lexicographically_smallest_word(word)

# Output the result
print(result)
# Generator time: 16.7123 seconds