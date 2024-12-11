def main():
    # Read the input string
    input_string = input()

    # Initialize counters for each category
    whitespace_count = 0
    lowercase_count = 0
    uppercase_count = 0
    symbol_count = 0

    # Iterate over each character in the input string
    for char in input_string:
        if char == '_':
            whitespace_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            symbol_count += 1

    # Calculate the total number of characters
    total_characters = len(input_string)

    # Calculate the ratios
    whitespace_ratio = whitespace_count / total_characters
    lowercase_ratio = lowercase_count / total_characters
    uppercase_ratio = uppercase_count / total_characters
    symbol_ratio = symbol_count / total_characters

    # Print the ratios
    print(whitespace_ratio)
    print(lowercase_ratio)
    print(uppercase_ratio)
    print(symbol_ratio)

if __name__ == "__main__":
    main()