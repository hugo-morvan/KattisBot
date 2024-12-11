from datetime import datetime

def is_halloween(date_str):
    # Convert the input string to a datetime object
    date_obj = datetime.strptime(date_str, "%b %d")
    
    # Define the Halloween dates
    halloween_dates = {
        "OCT": 31,
        "DEC": 25
    }
    
    # Check if the date matches any of the Halloween dates
    if date_obj.month == halloween_dates.get(date_obj.strftime("%b")):
        return "yup"
    else:
        return "nope"

# Read input from the user
input_date = input()

# Get the result and print it
result = is_halloween(input_date)
print(result)