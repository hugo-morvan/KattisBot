def rotate_char(c, n):
    if c == '_':
        return chr((ord(c) - ord('A') + n) % 28 + ord('A'))
    elif c == '.':
        return chr((ord(c) - ord('A') + n) % 28 + ord('A'))
    else:
        return chr((ord(c) - ord('A') + n) % 26 + ord('A'))

def encrypt_string(s, n):
    s = s[::-1]
    encrypted = ''.join(rotate_char(c, n) for c in s)
    return encrypted

def main():
    while True:
        line = input().strip()
        if line == '0':
            break
        N = int(line.split()[0])
        message = line.split()[1]
        result = encrypt_string(message, N)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 7.9830 seconds