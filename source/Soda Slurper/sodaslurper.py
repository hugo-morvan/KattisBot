# Read input values
e, f, c = map(int, input().split())

# Initialize variables
total_sodas_drunk = 0
current_bottles = e + f

# Simulate drinking sodas
while current_bottles >= c:
    # Calculate how many new sodas Tim can buy
    new_sodas = current_bottles // c
    total_sodas_drunk += new_sodas
    
    # Update the number of bottles Tim has
    current_bottles = new_sodas + (current_bottles % c)

# Print the total number of sodas Tim drank
print(total_sodas_drunk)