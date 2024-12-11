def reverse_binary(n):
    # Convert the number to its binary representation, remove the '0b' prefix, and reverse it
    reversed_bin = bin(n)[2:][::-1]
    # Convert the reversed binary string back to an integer
    return int(reversed_bin, 2)

# Read the input number
N = int(input())

# Calculate the reversed binary representation and output the result
print(reverse_binary(N))