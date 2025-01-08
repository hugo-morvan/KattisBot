def reverse_string(s):
    return s[::-1]

def find_best_word(word):
    n = len(word)
    best_word = word
    
    for i in range(1, n-1):
        for j in range(i+1, n):
            part1 = word[:i]
            part2 = word[i:j]
            part3 = word[j:]
            
            reversed_part1 = reverse_string(part1)
            reversed_part2 = reverse_string(part2)
            reversed_part3 = reverse_string(part3)
            
            candidate_word = reversed_part1 + reversed_part2 + reversed_part3
            if candidate_word < best_word:
                best_word = candidate_word
    
    return best_word

# Read input
word = input().strip()

# Find and print the best word
best_word = find_best_word(word)
print(best_word)
# Generator time: 23.1626 seconds