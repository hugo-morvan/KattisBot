def serve_drinks():
    # Read input values
    n, m = map(int, input().split())
    drinks = [input() for _ in range(n)]
    orders = [input() for _ in range(m)]

    # Create a dictionary to keep track of customer's drink order progress
    customer_orders = {customer: 0 for customer in orders}

    # Initialize the result list to store the served drinks
    served_drinks = []

    # Iterate over each order
    for order in orders:
        # Find the index of the current drink in the menu
        current_index = drinks.index(order)
        
        # If this is the first order for this customer, add the drink to the served list
        if customer_orders[order] == 0:
            served_drinks.append(drink)
            customer_orders[order] += 1
        
        # Otherwise, skip the drink and move to the next one in the menu
        else:
            served_drinks.append(drinks[current_index + 1])
            customer_orders[order] += 1

    # Print the served drinks in the correct order
    for drink in served_drinks:
        print(drink)

# Call the function to serve drinks
serve_drinks()