def is_champernowne_word(n):
    # Calculate the number of digits in the Champernowne word up to the k-th digit
    def count_digits(k):
        if k <= 9:
            return k
        elif k <= 99:
            return 18 + (k - 9)
        elif k <= 999:
            return 270 + (k - 99) * 2
        elif k <= 9999:
            return 3600 + (k - 999) * 3
        elif k <= 99999:
            return 45000 + (k - 9999) * 4
        elif k <= 999999:
            return 540000 + (k - 99999) * 5
        elif k <= 9999999:
            return 6300000 + (k - 999999) * 6
        elif k <= 99999999:
            return 72000000 + (k - 9999999) * 7
        else:
            return 810000000 + (k - 99999999) * 8

    # Find the word index
    k = 1
    while True:
        if count_digits(k) >= n:
            break
        k += 1

    # Check if the n-th digit is in the correct position
    current_number = 1
    for _ in range(k - 1):
        current_number *= 10

    # Convert the current number to a string and check the n-th digit
    current_str = str(current_number)
    if n <= len(current_str):
        return k
    else:
        return -1

# Read input
n = int(input())

# Output the result
print(is_champernowne_word(n))