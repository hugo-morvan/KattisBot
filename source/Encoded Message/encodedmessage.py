def decode_message(encoded_message):
    # Calculate the side length of the square
    n = int(len(encoded_message) ** 0.5)
    
    # Create a 2D list to represent the square
    square = [[''] * n for _ in range(n)]
    
    # Fill the square with the encoded message
    for i in range(n):
        for j in range(n):
            square[i][j] = encoded_message[i * n + j]
    
    # Rotate the square 90 degrees clockwise
    rotated_square = [''.join(row[::-1]) for row in zip(*square)]
    
    # Join the rows to form the original message
    decoded_message = ''.join(''.join(row) for row in rotated_square)
    
    return decoded_message

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    # Read the encoded message
    encoded_message = input()
    
    # Decode the message
    decoded_message = decode_message(encoded_message)
    
    # Print the decoded message
    print(decoded_message)