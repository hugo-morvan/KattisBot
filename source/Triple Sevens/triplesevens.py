# Read input
n = int(input())
digits = [input().split()]

# Check if all wheels can show the digit '7'
if all('7' in digit for digit in digits):
    print("777")
else:
    print("0")