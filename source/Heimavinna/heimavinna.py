def count_problems(input_string):
    # Split the input string by semicolons
    parts = input_string.split(';')
    
    total_count = 0
    
    for part in parts:
        if '-' in part:
            # Handle ranges like 1-3
            start, end = map(int, part.split('-'))
            total_count += end - start + 1
        else:
            # Handle individual numbers like 1
            total_count += 1
    
    return total_count

# Read input
input_string = input()

# Calculate and print the number of problems
print(count_problems(input_string))