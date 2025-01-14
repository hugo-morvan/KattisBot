# XOR Calculation
def xor(a, b):
	return a ^ b;

# Input Variables
N = int(input())
a = int(input())
b = int(input())

# Calculate XOR of all numbers from 1 to N and print the result
print(xor(xor(xor(xor(xor(xor(xor(xor(xor(xor(0, N), N-1), N-2), N-3), N-4), N-5), N-6), N-7), N-8), N-9))
# Generator time: 5.8345 seconds