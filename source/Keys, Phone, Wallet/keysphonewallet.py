def find_missing_items(n):
    # Define the set of required items
    required_items = {'keys', 'phone', 'wallet'}
    
    # Read the input items
    input_items = set()
    for _ in range(n):
        input_items.add(input())
    
    # Find missing items
    missing_items = required_items - input_items
    
    # Output the missing items in alphabetical order
    if missing_items:
        for item in sorted(missing_items):
            print(item)
    else:
        print("ready")

# Read the number of items
n = int(input())

# Call the function with the number of items
find_missing_items(n)