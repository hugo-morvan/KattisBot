def multiply_nonzero_digits(x):
    while x > 9:
        product = 1
        for digit in str(x):
            if digit != '0':
                product *= int(digit)
        x = product
    return x

# Read input
x = int(input())

# Get the resulting digit
resulting_digit = multiply_nonzero_digits(x)

# Print the result
print(resulting_digit)