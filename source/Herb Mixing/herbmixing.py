def max_health_boost(green_herbs, red_herbs):
    # Define the boost values for each recipe
    boost_values = [1, 3, 10, 10]
    
    # Calculate the maximum health boost from green herbs
    max_green_boost = min(3, green_herbs) * boost_values[2] + \
                      min(2, green_herbs % 3) * boost_values[1] + \
                      green_herbs % 3 * boost_values[0]
    
    # Calculate the maximum health boost from red herbs
    max_red_boost = red_herbs * boost_values[3]
    
    # Total maximum health boost
    total_boost = max_green_boost + max_red_boost
    
    return total_boost

# Read input
green_herbs, red_herbs = map(int, input().split())

# Calculate and print the maximum health boost
print(max_health_boost(green_herbs, red_herbs))