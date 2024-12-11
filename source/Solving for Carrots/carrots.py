def calculate_carrots(n_contestants, p_huffle_puff):
    # Initialize the total number of carrots to zero
    total_carrots = 0
    
    # Iterate through each contestant
    for _ in range(n_contestants):
        # Read the description of the contestant
        description = input()
        
        # Check if the description contains "huffle-puff"
        if "huffle-puff" in description.lower():
            # If it does, increment the total number of carrots by 1
            total_carrots += 1
    
    # Print the total number of carrots
    print(total_carrots)

# Read the input values
n_contestants, p_huffle_puff = map(int, input().split())
calculate_carrots(n_contestants, p_huffle_puff)