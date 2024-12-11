# Read the input number
number = int(input())

# Extract the prefix number (first three digits)
prefix = number // 1000

# Check if the prefix is 555
if prefix == 555:
    print(1)
else:
    print(0)