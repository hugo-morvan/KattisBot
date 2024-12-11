def convert_long_to_short(notation):
    # Split the notation by hyphen
    parts = notation.split('-')
    
    # Take the first letter of each part and join them
    short_notation = ''.join(part[0] for part in parts)
    
    return short_notation

# Read input
notation = input()

# Convert and print the result
print(convert_long_to_short(notation))