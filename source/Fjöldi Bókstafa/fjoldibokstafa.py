# Read the input string
input_string = input()

# Initialize a counter for letters
letter_count = 0

# Iterate through each character in the string
for char in input_string:
    # Check if the character is a letter (either lowercase or uppercase)
    if char.isalpha():
        # Increment the letter counter
        letter_count += 1

# Print the total number of letters
print(letter_count)