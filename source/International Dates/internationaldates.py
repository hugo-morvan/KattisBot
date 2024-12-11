date = input()

# Split the date into components
month, day, year = map(int, date.split('/'))

# Check if the date is in the US format (MM/DD/YYYY)
if 1 <= month <= 12 and 1 <= day <= 31:
    print("US")
else:
    # Check if the date is in the European format (DD/MM/YYYY)
    if 1 <= day <= 12 and 1 <= month <= 31:
        print("EU")
    else:
        print("either")