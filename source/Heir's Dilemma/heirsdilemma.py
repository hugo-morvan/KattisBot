def count_combinations(L, H):
    def is_valid_combination(c):
        # Convert the number to a string to easily access each digit
        c_str = str(c)
        # Check if all digits are different
        if len(set(c_str)) != 6:
            return False
        # Check if the number is divisible by each of its digits
        for digit in c_str:
            if int(digit) == 0 or c % int(digit) != 0:
                return False
        return True

    count = 0
    for c in range(L, H + 1):
        if is_valid_combination(c):
            count += 1

    return count

# Read input
L, H = map(int, input().split())

# Calculate and print the result
print(count_combinations(L, H))