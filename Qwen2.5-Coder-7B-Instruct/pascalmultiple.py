def count_multiples_of_k_in_pascals_triangle(N, K):
    # Initialize a list to store binomial coefficients
    C = [[0 for _ in range(i + 1)] for i in range(N + 1)]
    
    # Base case: C(0,0) = 1
    C[0][0] = 1
    
    # Fill Pascal's triangle using the given recurrence relation
    for i in range(1, N + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i-1][j] + C[i-1][j-1]) % K
    
    # Count the number of entries that are multiples of K
    count_multiples = sum(row.count(0) for row in C)
    
    return count_multiples

# Read input values
N, K = map(int, input().split())

# Compute and print the result
result = count_multiples_of_k_in_pascals_triangle(N, K)
print(result)
# Generator time: 7.9064 seconds