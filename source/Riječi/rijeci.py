def count_letters(K):
    # Initialize the counts of 'A' and 'B'
    count_A = 0
    count_B = 0
    
    # Iterate over each press of the button
    for i in range(K):
        if i % 2 == 0:
            # If the press is even, add 'A' to count_A
            count_A += 1
        else:
            # If the press is odd, add 'B' to count_B
            count_B += 1
    
    return count_A, count_B

# Read the input value of K
K = int(input())

# Calculate the number of 'A' and 'B'
count_A, count_B = count_letters(K)

# Print the result
print(count_A, count_B)