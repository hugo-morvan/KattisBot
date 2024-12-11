import sys

# Read input
input_data = [input().strip() for _ in range(5)]

# Find CIA blimps
cias = [index + 1 for index, code in enumerate(input_data) if 'FBI' in code]

# Print result
if cias:
    print(' '.join(map(str, cias)))
else:
    print("HE GOT AWAY!")