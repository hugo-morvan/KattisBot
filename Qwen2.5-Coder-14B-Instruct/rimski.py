def roman_to_value(c):
    if c == 'I':
        return 1
    elif c == 'V':
        return 5
    elif c == 'X':
        return 10
    elif c == 'L':
        return 50
    else:
        raise ValueError("Invalid Roman numeral character")

def value_to_roman(v):
    if v == 1:
        return 'I'
    elif v == 5:
        return 'V'
    elif v == 10:
        return 'X'
    elif v == 50:
        return 'L'
    else:
        raise ValueError("Invalid value for conversion to Roman numeral")

def smallest_roman_number(roman):
    values = [roman_to_value(c) for c in roman]
    values.sort()
    
    result = ""
    for v in values:
        result += value_to_roman(v)
    
    return result

# Read input
B = input().strip()

# Get the smallest rearrangement of Roman numerals
smallest_Roman = smallest_roman_number(B)

# Print the result
print(smallest_Roman)
# Generator time: 31.3988 seconds