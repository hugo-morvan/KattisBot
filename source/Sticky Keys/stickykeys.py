def correct_message(message):
    result = []
    previous_char = None
    
    for char in message:
        if char != ' ' and (previous_char is None or char != previous_char):
            result.append(char)
        previous_char = char
    
    return ''.join(result)

# Read input
input_message = input()

# Correct the message
corrected_message = correct_message(input_message)

# Output the corrected message
print(corrected_message)