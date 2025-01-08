MOD = 10**9 + 7

def min_cost(prime_factors):
    K = 1
    for i in range(0, len(prime_factors), 2):
        K *= int(prime_factors[i]) ** int(prime_factors[i+1])
    
    # Find the smallest M such that M^x = K for some integer x
    M = 1
    while M**2 <= K:
        if K % M == 0:
            x = 0
            temp = K
            while temp % M == 0:
                x += 1
                temp //= M
            
            # Check if this is the smallest M found so far
            if x > 0 and (M**x == K):
                break
        M += 1
    
    # Calculate the cost
    base_cost = M
    purchase_cost = x * M
    total_cost = (base_cost + purchase_cost) % MOD
    
    return total_cost

# Read input
prime_factors = input().strip()

# Output the result
print(min_cost(prime_factors))
# Generator time: 8.4593 seconds