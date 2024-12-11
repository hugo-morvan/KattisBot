# Read two three-digit numbers
A = int(input())
B = int(input())

# Convert numbers to strings for easy manipulation
A_str = str(A)
B_str = str(B)

# Reverse the strings
A_reversed = A_str[::-1]
B_reversed = B_str[::-1]

# Compare the reversed numbers
if A_reversed > B_reversed:
    print(A_reversed)
else:
    print(B_reversed)