import random

def hangman_game(word, permutation):
    word = list(word)
    drawing = [""] * 10
    guessed_letters = set()
    
    for letter in permutation:
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    drawing[i] = letter
        else:
            drawing.append(letter)
        
        if "".join(drawing) == word:
            return "WIN"
        
        guessed_letters.add(letter)
        
        if len(guessed_letters) == 26:
            return "LOSE"

word = input().strip()
permutation = input().strip()
result = hangman_game(word, permutation)
print(result)