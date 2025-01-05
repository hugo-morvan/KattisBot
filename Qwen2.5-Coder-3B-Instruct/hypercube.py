def gray_code_distance(n, a, b):
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Calculate the distance between the two integers in the Gray Code
    distance = abs(int_a - int_b)
    
    return distance

# Read input
n = int(input())
a = input()
b = input()

# Calculate and print the distance
print(gray_code_distance(n, a, b))
# Generator time: 7.2862 seconds