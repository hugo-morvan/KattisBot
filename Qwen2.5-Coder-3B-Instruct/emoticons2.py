def calculate_min_max_lengths(message):
    # Define the mapping of emoticons to emojis
    emoticon_to_emoji = {
        '):': ':)',
        ':-)': ':-)',
        ':-((': ':-((',
        ';-)': ';-)',
        'xD': 'xD',
        '^_^': '^_^',
        '-_-': '-_-',
        '^o^': '^o^',
        '^^;': '^^;',
        '(..)': '(..)'
    }
    
    # Initialize variables to store the minimum and maximum lengths
    min_length = len(message)
    max_length = len(message)
    
    # Iterate over the message to find all emoticons
    i = 0
    while i < len(message):
        for emoticon, emoji in emoticon_to_emoji.items():
            if message[i:i+len(emoticon)] == emoticon:
                # Calculate the length if the emoticon is replaced
                new_length = len(message[:i]) + len(emoji) + len(message[i+len(emoticon):])
                min_length = min(min_length, new_length)
                max_length = max(max_length, new_length)
                # Skip past the current emoticon
                i += len(emoticon)
                break
        else:
            # If no emoticon is found, move to the next character
            i += 1
    
    return min_length, max_length

# Read the input message
message = input().strip()

# Calculate the minimum and maximum lengths
min_length, max_length = calculate_min_max_lengths(message)

# Print the result
print(min_length, max_length)
# Generator time: 24.2381 seconds