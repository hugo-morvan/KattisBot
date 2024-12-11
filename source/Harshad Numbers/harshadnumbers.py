def next_harshad_number(n):
    while True:
        if n % sum(int(digit) for digit in str(n)) == 0:
            return n
        n += 1

# Read input
n = int(input())

# Find and print the next harshad number
print(next_harshad_number(n))