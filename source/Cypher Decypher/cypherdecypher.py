def encode_message(secret_multiplier, messages):
    # Mapping from numbers to characters
    char_map = {str(i): chr(ord('A') + i % 26) for i in range(26)}
    
    def decrypt_number(number_str):
        return int(number_str)
    
    def encrypt_message(message, secret_multiplier):
        encrypted_message = []
        for char in message:
            # Convert character to its corresponding number
            char_num = decrypt_number(char_map[char])
            # Multiply with the secret multiplier
            multiplied_num = char_num * int(secret_multiplier)
            # Convert back to character
            encrypted_char = char_map[str(multiplied_num % 26)]
            encrypted_message.append(encrypted_char)
        return ''.join(encrypted_message)
    
    results = []
    for message in messages:
        encrypted = encrypt_message(message, secret_multiplier)
        results.append(encrypted)
    
    return results

# Read input
secret_multiplier = input()
n = int(input())
messages = [input() for _ in range(n)]

# Encode messages
encoded_messages = encode_message(secret_multiplier, messages)

# Print output
for encrypted in encoded_messages:
    print(encrypted)