def count_multiples_of_k_in_pascals_triangle(N, K):
    # Initialize a 2D list to store binomial coefficients
    C = [[0] * (i + 1) for i in range(N + 1)]
    
    # Fill the first row of Pascal's triangle
    C[0][0] = 1
    
    # Fill the rest of the triangle using the recurrence relation
    for i in range(1, N + 1):
        C[i][0] = 1
        for j in range(1, i):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % K
        C[i][i] = 1
    
    # Count the number of entries divisible by K
    count = 0
    for i in range(N + 1):
        for j in range(i + 1):
            if C[i][j] == 0:
                count += 1
    
    return count

# Read input values
N, K = map(int, input().split())

# Calculate and print the result
print(count_multiples_of_k_in_pascals_triangle(N, K))
# Generator time: 33.6384 seconds