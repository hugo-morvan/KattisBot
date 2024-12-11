def count_vowels(word):
    vowels = "aeiou"
    count_y_not = sum(1 for char in word if char in vowels)
    count_y_yes = sum(1 for char in word if char in vowels + 'y')
    print(count_y_not, count_y_yes)

# Read input
word = input()

# Call the function
count_vowels(word)