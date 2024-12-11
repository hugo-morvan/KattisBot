# Read input values
cost_per_sqm = float(input())
num_lawns = int(input())

# Initialize total cost
total_cost = 0.0

# Process each lawn
for _ in range(num_lawns):
    width, length = map(float, input().split())
    # Calculate the area of the lawn
    area = width * length
    # Add the cost for this lawn to the total cost
    total_cost += cost_per_sqm * area

# Print the total cost
print(total_cost)