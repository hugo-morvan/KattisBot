# Read 10 numbers from input
numbers = [int(input()) for _ in range(10)]

# Calculate the modulo 42 of each number
modulos = [num % 42 for num in numbers]

# Use a set to find distinct values
distinct_modulos = set(modulos)

# Output the number of distinct values
print(len(distinct_modulos))