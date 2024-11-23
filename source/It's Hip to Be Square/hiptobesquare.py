
import math

def max_layers(N):
    # Calculate the largest possible side length of the square
    max_side_length = int(math.sqrt(N))
    
    # Check if the largest square can have a 1x1 empty space in the middle
    if (max_side_length + 1) ** 2 <= N:
        return max_side_length - 1
    else:
        return max_side_length

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    result = max_layers(N)
    print(result)
