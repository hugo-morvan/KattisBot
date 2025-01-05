def encode_string(N, message):
    # Define the alphabet with underscore and period
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    
    # Reverse the message
    reversed_message = message[::-1]
    
    # Encode the reversed message
    encoded_message = ''.join(alphabet[(alphabet.index(char) + N) % len(alphabet)] for char in reversed_message)
    
    return encoded_message

# Read input
T = int(input())
while T > 0:
    N = int(input())
    message = input()
    
    # Encode the message
    encoded = encode_string(N, message)
    
    # Print the result
    print(encoded)
    
    # Read the next test case or break if the input is 0
    T = int(input()) if T > 1 else 0
# Generator time: 9.4465 seconds