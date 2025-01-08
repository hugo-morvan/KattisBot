def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)

def convert_emoticons_to_emoji(text):
    emoticons = {
        ':)': '😊',
        ':-)': '😊',
        ':-((': '😢',
        ';-)': '😉',
        'xD': '😆',
        '^_^': '🙂',
        '-_-': '😐',
        '^o^': '😍',
        '^^;': '😅',
        '(..)': '👀'
    }
    
    for emoticon, emoji in emoticons.items():
        text = text.replace(emoticon, emoji)
    
    return len(text)

def find_min_max_message_length(original_text):
    min_length = float('inf')
    max_length = float('-inf')
    
    visible_chars_and_space = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~"
    
    for old_char in visible_chars_and_space:
        for new_char in visible_chars_and_space:
            modified_text = replace_char(original_text, old_char, new_char)
            length_after_conversion = convert_emoticons_to_emoji(modified_text)
            
            if length_after_conversion < min_length:
                min_length = length_after_conversion
            if length_after_conversion > max_length:
                max_length = length_after_conversion
    
    return min_length, max_length

# Read input
original_text = input().strip()

# Find and print the minimum and maximum possible message lengths
min_length, max_length = find_min_max_message_length(original_text)
print(min_length, max_length)
# Generator time: 46.7903 seconds