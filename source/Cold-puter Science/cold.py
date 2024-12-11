# Read the number of temperatures
n = int(input())

# Read the temperatures
temperatures = list(map(int, input().split()))

# Count the number of temperatures below zero
count_below_zero = sum(1 for temp in temperatures if temp < 0)

# Print the result
print(count_below_zero)