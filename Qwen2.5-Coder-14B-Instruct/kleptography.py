def autokey_decrypt(n, m, last_n_plaintext, ciphertext):
    # Convert the last n letters of the plaintext to their corresponding numbers
    key = [ord(char) - ord('a') for char in last_n_plaintext]
    
    # Decrypt the first part of the ciphertext using the key
    plaintext = []
    for i in range(n):
        decrypted_char = (ciphertext[i] - key[i]) % 26
        plaintext.append(chr(decrypted_char + ord('a')))
        key.append(decrypted_char)
    
    # Decrypt the rest of the ciphertext using the autokey method
    for i in range(n, m):
        decrypted_char = (ciphertext[i] - key[i - n]) % 26
        plaintext.append(chr(decrypted_char + ord('a')))
        key.append(decrypted_char)
    
    return ''.join(plaintext)

# Read input
n, m = map(int, input().split())
last_n_plaintext = input()
ciphertext = [ord(char) - ord('a') for char in input()]

# Decrypt the ciphertext
plaintext = autokey_decrypt(n, m, last_n_plaintext, ciphertext)

# Output the plaintext
print(plaintext)
# Generator time: 34.2886 seconds