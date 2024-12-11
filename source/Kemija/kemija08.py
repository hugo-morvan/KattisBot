def decode_sentence(coded_sentence):
    vowels = 'aeiou'
    decoded_sentence = []
    
    for word in coded_sentence.split():
        decoded_word = []
        i = 0
        while i < len(word):
            if word[i] in vowels:
                decoded_word.append(word[i])
                decoded_word.append('p')
                decoded_word.append(word[i])
                i += 3
            else:
                decoded_word.append(word[i])
                i += 1
        decoded_sentence.append(''.join(decoded_word))
    
    return ' '.join(decoded_sentence)

# Read input
coded_sentence = input()

# Decode the sentence
decoded_sentence = decode_sentence(coded_sentence)

# Print the output
print(decoded_sentence)