def next_larger_number(X):
    # Convert the number to a list of digits
    digits = list(str(X))
    
    # Traverse the digits from right to left
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            # Find the smallest digit greater than digits[i - 1]
            for j in range(len(digits) - 1, i - 1, -1):
                if digits[j] > digits[i - 1]:
                    # Swap the found digit with digits[i - 1]
                    digits[i - 1], digits[j] = digits[j], digits[i - 1]
                    
                    # Sort the digits after i - 1 in ascending order
                    digits[i:] = sorted(digits[i:])
                    
                    # Convert the list of digits back to an integer
                    return int(''.join(digits))
    
    # If no larger number is found, return 0
    return 0

# Read input
X = int(input())

# Get the next larger number
result = next_larger_number(X)

# Print the result
print(result)