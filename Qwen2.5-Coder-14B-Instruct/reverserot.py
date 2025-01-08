def rotate_char(c, n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    index = (alphabet.index(c) + n) % len(alphabet)
    return alphabet[index]

def encode_message(N, message):
    # Reverse the message
    reversed_message = message[::-1]
    # Rotate each character by N positions
    encoded_message = ''.join(rotate_char(c, N) for c in reversed_message)
    return encoded_message

# Read input until 0 is encountered
while True:
    line = input().strip()
    if line == "0":
        break
    
    parts = line.split()
    N = int(parts[0])
    message = parts[1]
    
    encrypted_message = encode_message(N, message)
    print(encrypted_message)
# Generator time: 22.6972 seconds