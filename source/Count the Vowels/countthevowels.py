def count_vowels(s):
    vowels = "AEIOUaeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Read input
input_text = input()

# Count vowels
vowel_count = count_vowels(input_text)

# Print output
print(vowel_count)