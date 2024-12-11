def sum_of_squares_of_digits(base, number):
    # Convert the number to the given base
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    
    # Calculate the sum of squares of the digits
    return sum(digit ** 2 for digit in digits)

# Read the number of test cases
P = int(input())

for k in range(1, P + 1):
    # Read the base and number
    _, base, number = map(int, input().split())
    
    # Compute the Sum of Squared Digits
    result = sum_of_squares_of_digits(base, number)
    
    # Print the result
    print(f"{k} {result}")