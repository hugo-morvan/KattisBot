# Read the input string
input_string = input()

# Initialize an empty list to store the result
result = []

# Iterate through each character in the input string
for char in input_string:
    # Check if the result list is empty or the last character is different from the current one
    if not result or result[-1] != char:
        # Append the current character to the result list
        result.append(char)

# Join the list into a string and print it
print(''.join(result))