import re

def calculate_average_heart_rate(customer_data):
    # Split the input into individual customer data entries
    entries = customer_data.split('\n')
    
    # Initialize a dictionary to store the total heart rate and count for each customer
    customer_averages = {}
    
    for entry in entries:
        # Use regular expression to find all heart rate values in the entry
        heart_rates = re.findall(r'\d+\.\d+', entry)
        
        # If there are no heart rates, skip to the next entry
        if not heart_rates:
            continue
        
        # Calculate the average heart rate for this customer
        total_hr = sum(float(hr) for hr in heart_rates)
        count = len(heart_rates)
        average_hr = round(total_hr / count, 4)
        
        # Find the customer name in the entry
        name_match = re.search(r'[^0-9\s]+', entry)
        if name_match:
            customer_name = name_match.group()
        else:
            customer_name = "Unknown"
        
        # Store the average heart rate in the dictionary
        customer_averages[customer_name] = average_hr
    
    # Print the results in the required format
    for name, avg_hr in customer_averages.items():
        print(f"{avg_hr:.4f} {name}")

# Read input from the user
input_data = input()

# Call the function to process the input and generate the report
calculate_average_heart_rate(input_data)