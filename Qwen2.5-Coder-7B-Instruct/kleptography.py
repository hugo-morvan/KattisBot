def decrypt_autokey_cipher(n, m, last_n_letters, ciphertext):
    key = list(last_n_letters)
    plaintext = []
    
    for i in range(m):
        a_i = ord(ciphertext[i]) - ord('a')
        k_i = ord(key[i % n]) - ord('a')
        b_i = (a_i - k_i) % 26
        plaintext.append(chr(b_i + ord('a')))
    
    return ''.join(plaintext)

# Read input
n, m = map(int, input().split())
last_n_letters = input().strip()
ciphertext = input().strip()

# Output the decrypted plaintext
print(decrypt_autokey_cipher(n, m, last_n_letters, ciphertext))
# Generator time: 6.0945 seconds