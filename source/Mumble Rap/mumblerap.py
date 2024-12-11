def find_largest_number(s):
    max_number = 0
    current_number = 0
    
    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            if current_number > max_number:
                max_number = current_number
            current_number = 0
    
    # Check the last number if the string ends with a digit
    if current_number > max_number:
        max_number = current_number
    
    return max_number

# Read input
N = int(input())
s = input()

# Find and print the largest number
print(find_largest_number(s))