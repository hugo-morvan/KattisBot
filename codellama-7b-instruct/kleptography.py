n, m = map(int, input().split())
a, b = input().lower(), input().lower()
key = a[0:n] + "".join(sorted(b))
cipher = [ord(i) - ord('a') for i in key]
plaintext = ''
for i in range(m):
    plaintext += chr((ord(b[i]) - cipher[i]) % 26 + ord('a'))
print(plaintext.lower())
# Generator time: 4.7915 seconds