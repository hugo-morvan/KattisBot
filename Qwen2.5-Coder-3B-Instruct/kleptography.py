def autokey_cipher(n, m, keyword, ciphertext):
    # Convert the keyword to a list of indices
    key_indices = [ord(char) - ord('a') for char in keyword]
    
    # Initialize the plaintext list
    plaintext = []
    
    # Iterate over the ciphertext
    for i in range(m):
        # Calculate the index for the current character in the ciphertext
        index = (ord(ciphertext[i]) - ord('a') - key_indices[i % n]) % 26
        
        # Append the corresponding character to the plaintext
        plaintext.append(chr(index + ord('a')))
    
    # Join the plaintext list into a string and print it
    print(''.join(plaintext))

# Read input values
n, m = map(int, input().split())
keyword = input()
ciphertext = input()

# Call the function to decrypt the ciphertext
autokey_cipher(n, m, keyword, ciphertext)
# Generator time: 8.8281 seconds