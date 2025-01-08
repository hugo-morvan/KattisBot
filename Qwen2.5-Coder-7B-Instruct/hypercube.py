def gray_code_distance(n, a, b):
    # Convert binary strings to integers for easier manipulation
    a_int = int(a, 2)
    b_int = int(b, 2)
    
    # Calculate the XOR of a and b
    xor_result = a_int ^ b_int
    
    # Count the number of set bits in the XOR result
    distance = bin(xor_result).count('1')
    
    return distance - 1

# Input
n = int(input())
a = input()
b = input()

# Output
print(gray_code_distance(n, a, b))
# Generator time: 5.4937 seconds