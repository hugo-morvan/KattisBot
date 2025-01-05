def next_smallest_with_same_digit_sum(N):
    # Convert N to a string to easily iterate over its digits
    str_N = str(N)
    
    # Calculate the digit sum of N
    digit_sum = sum(int(digit) for digit in str_N)
    
    # Start checking from N+1
    for i in range(N + 1, 10**len(str_N)):
        # Convert the current number to a string to check the digit sum
        str_i = str(i)
        if sum(int(digit) for digit in str_i) == digit_sum:
            return i

# Read input
N = int(input())

# Find and print the result
result = next_smallest_with_same_digit_sum(N)
print(result)
# Generator time: 14.0803 seconds