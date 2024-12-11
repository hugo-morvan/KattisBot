def max_layers(N):
    # Calculate the side length of the largest possible square
    side_length = int(N**0.5)
    
    # Calculate the number of layers
    layers = side_length - 1
    
    return layers

# Read input
T = int(input())
results = []

for _ in range(T):
    N = int(input())
    results.append(max_layers(N))

# Print results
for result in results:
    print(result)