def center_and_balance_sign(rows, cols, words):
    # Calculate the number of spaces needed for centering and balancing
    half_cols = cols // 2
    balance_offset = cols % 2
    
    # Process each word
    for i, word in enumerate(words):
        # Calculate the number of spaces needed on each side
        l = half_cols - (len(word) // 2)
        r = half_cols + (len(word) // 2) + (1 if i % 2 == 0 else 0)
        
        # Create the row with spaces
        row = '.' * l + word + '.' * r
        
        # Print the row
        print(row)

# Read input
r, c = map(int, input().split())
words = [input() for _ in range(r)]

# Process the sign
center_and_balance_sign(r, c, words)