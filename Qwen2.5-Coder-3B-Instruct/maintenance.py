def min_cost_to_store(K):
    # Parse the input string
    prime_factors = [int(input()) for _ in range(len(K) // 2)]
    
    # Calculate the minimum cost
    min_cost = float('inf')
    
    # Iterate over each prime factor
    for p in prime_factors:
        # Check for all possible server sizes M such that K = M * n
        for M in range(p, K + 1, p):
            if K % M == 0:
                # Calculate the cost
                cost = 2 * M
                # Update the minimum cost
                if cost < min_cost:
                    min_cost = cost
    
    # Return the minimum cost modulo 10^9 + 7
    return min_cost % (10**9 + 7)

# Example usage
input_string = input()
result = min_cost_to_store(input_string)
print(result)
# Generator time: 23.9613 seconds