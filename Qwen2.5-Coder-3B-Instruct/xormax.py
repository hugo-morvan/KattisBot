def max_xor_sum(n, numbers):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the maximum xor-sum to 0
    max_xor = 0
    
    # Iterate through the sorted list to calculate the xor-sum
    for num in numbers:
        max_xor ^= num
    
    return max_xor

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Calculate and print the result
print(max_xor_sum(n, numbers))
# Generator time: 16.4386 seconds