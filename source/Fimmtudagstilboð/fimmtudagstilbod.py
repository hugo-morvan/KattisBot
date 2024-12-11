# Read the input year
y = int(input())

# Calculate the price based on the given pattern
if y == 2020:
    price = 1000
elif 2020 <= y <= 2024:
    price = 1000 + (y - 2020) * 100
else:
    price = 1000 + (y - 2020) * 100

# Print the calculated price
print(price)