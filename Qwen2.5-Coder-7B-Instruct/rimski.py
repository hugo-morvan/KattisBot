# Mapping of Roman numerals to their integer values
roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100
}

def smallest_roman_numeral(num):
    # Convert the Roman numeral string to a list of integers
    num_list = [roman_values[char] for char in num]
    
    # Sort the list in ascending order
    num_list.sort()
    
    # Convert the sorted list back to a Roman numeral string
    result = ''.join([list(roman_values.keys())[i] for i in range(len(num_list))])
    
    return result

# Read input from user
B = input().strip()

# Output the smallest possible number
print(smallest_roman_numeral(B))
# Generator time: 6.5783 seconds