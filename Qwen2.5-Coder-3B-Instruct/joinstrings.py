def process_operations(n, strings, operations):
    # Convert strings to a list for easier manipulation
    str_list = [s for s in strings]
    
    # Process each operation
    for a, b in operations:
        # Concatenate S_b to S_a
        str_list[a - 1] += str_list[b - 1]
        # Make S_b empty
        str_list[b - 1] = ""
    
    # Return the final string
    return str_list[0]

# Read input
n = int(input())
strings = [input() for _ in range(n)]
operations = [(int(a), int(b)) for _ in range(n - 1)]

# Process the operations and print the result
result = process_operations(n, strings, operations)
print(result)
# Generator time: 16.3132 seconds