def can_guess_operation(s):
    # Check if the string is already in sorted order
    if s == ''.join(sorted(s)):
        return 1
    
    # Check if the string has more than one distinct character
    if len(set(s)) > 1:
        return 1
    
    # If the string has exactly one distinct character, it cannot be sorted by swapping
    return 0

# Read input
s = input()

# Output the result
print(can_guess_operation(s))