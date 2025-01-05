def roman_to_int(roman):
    # Define a mapping of Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Convert the Roman numeral to an integer
    value = 0
    i = 0
    while i < len(roman):
        current_value = roman_values[roman[i]]
        next_value = roman_values.get(roman[i + 1], 0)
        
        if current_value >= next_value:
            value += current_value
            i += 1
        else:
            value -= current_value
            i += 2
    
    return value

def int_to_roman(num):
    # Define a mapping of integer values to their Roman numeral symbols
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    # Convert the integer to a Roman numeral
    roman = ''
    for value, symbol in roman_numerals:
        while num >= value:
            roman += symbol
            num -= value
    return roman

# Read input
input_number = input()

# Convert the input Roman numeral to an integer
integer_value = roman_to_int(input_number)

# Convert the integer value back to the smallest possible Roman numeral
smallest_roman = int_to_roman(integer_value)

# Output the result
print(smallest_roman)
# Generator time: 23.1402 seconds