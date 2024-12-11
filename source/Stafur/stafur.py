def check_vowel(letter):
    vowels = "AEIOU"
    if letter in vowels:
        return "Jebb"
    elif letter == 'Y':
        return "Neibb"
    else:
        return "Kannski"

# Read input
input_letter = input()

# Get the result based on the input letter
result = check_vowel(input_letter)

# Print the result
print(result)