def validate_cpr_number(cpr_number):
    # Split the CPR number into day, month, year, and sequence number
    parts = cpr_number.split('-')
    day = int(parts[0][:2])
    month = int(parts[0][2:4])
    year = int(parts[0][4:])
    sequence_number = int(parts[1])

    # Calculate the checksum using the modulo 11 rule
    weights = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    checksum = sum(weight * int(digit) for weight, digit in zip(weights, cpr_number[:-1]))
    
    # Check if the checksum is divisible by 11
    if checksum % 11 == 0:
        return "1"
    else:
        return "0"

# Read input
cpr_number = input()

# Validate the CPR number and print the result
print(validate_cpr_number(cpr_number))