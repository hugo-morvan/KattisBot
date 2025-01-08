def max_xor_subset(n, numbers):
    # Initialize the maximum XOR result to 0
    max_xor = 0
    
    # Iterate over each number in the list
    for num in numbers:
        # Update the max_xor by considering the current number
        # This is done using a trick with XOR and bitwise operations
        # We try to update the bits from the highest to the lowest
        for i in range(64, -1, -1):
            if (max_xor | (1 << i)) <= num:
                max_xor |= (1 << i)
    
    return max_xor

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Calculate and print the result
print(max_xor_subset(n, numbers))
# Generator time: 23.1162 seconds