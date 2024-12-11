def find_lexicographically_smallest_word(R, C, crossword):
    def is_valid_word(word):
        return len(word) >= 2

    def get_horizontal_words(row):
        words = []
        current_word = ""
        for char in row:
            if char == "#":
                if current_word:
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += char
        if current_word:
            words.append(current_word)
        return words

    def get_vertical_words(col):
        words = []
        current_word = ""
        for i in range(R):
            char = crossword[i][col]
            if char == "#":
                if current_word:
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += char
        if current_word:
            words.append(current_word)
        return words

    smallest_word = None

    # Check horizontal words
    for row in crossword:
        words = get_horizontal_words(row)
        for word in words:
            if is_valid_word(word):
                if smallest_word is None or word < smallest_word:
                    smallest_word = word

    # Check vertical words
    for col in range(C):
        words = get_vertical_words(col)
        for word in words:
            if is_valid_word(word):
                if smallest_word is None or word < smallest_word:
                    smallest_word = word

    return smallest_word

# Read input
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

# Find and print the lexicographically smallest word
smallest_word = find_lexicographically_smallest_word(R, C, crossword)
print(smallest_word)