def swap_digits(code):
    # Convert the code from string to integers
    num1 = int(code[0])
    num2 = int(code[1])
    
    # Swap the digits
    swapped_code = str(num2) + str(num1)
    
    return swapped_code

# Read the input code
code = input()

# Get the swapped code
swapped_code = swap_digits(code)

# Print the swapped code
print(swapped_code)