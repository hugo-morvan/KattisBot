def gray_code_distance(n, a, b):
    def hamming_distance(x, y):
        return sum(c1 != c2 for c1, c2 in zip(x, y))
    
    def gray_to_binary(gray_str):
        binary = ''
        for bit in gray_str:
            if bit == '0':
                binary += binary[-1] if binary else '0'
            else:
                binary += str(1 - int(binary[-1])) if binary else '1'
        return binary
    
    # Convert Gray Code to Binary
    a_bin = gray_to_binary(a)
    b_bin = gray_to_binary(b)
    
    # Calculate the Hamming distance between the two binary strings
    return hamming_distance(a_bin, b_bin)

# Read input
n = int(input())
a = input().strip()
b = input().strip()

# Output the number of code words between a and b in the n-bit Gray Code
print(gray_code_distance(n, a, b))
# Generator time: 28.7521 seconds