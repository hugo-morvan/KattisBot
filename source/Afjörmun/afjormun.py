import sys

def unmeme_sentence(sentence):
    words = sentence.split()
    unmemed_words = []
    for word in words:
        if word[0].islower():
            unmemed_words.append(word.capitalize())
        else:
            unmemed_words.append(word.lower())
    return ' '.join(unmemed_words)

n = int(input().strip())
for _ in range(n):
    sentence = input().strip()
    unmemed_sentence = unmeme_sentence(sentence)
    print(unmemed_sentence)