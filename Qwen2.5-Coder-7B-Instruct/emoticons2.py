def min_max_message_length(text):
    emoticons = {':)', ':-', ':-(', ';-)', 'xD', '^_^', '-_-', '^o^', '^^;', '(..)'}
    min_length = len(text)
    max_length = 0
    
    for i in range(len(text)):
        if text[i] == ' ':
            continue
        for emoticon in emoticons:
            if text[i:].startswith(emoticon):
                max_length += len(emoticon) - 1
                break
        else:
            min_length += 1
            
    return min_length, max_length

# Input
text = input().strip()

# Output
min_length, max_length = min_max_message_length(text)
print(min_length, max_length)
# Generator time: 7.2883 seconds