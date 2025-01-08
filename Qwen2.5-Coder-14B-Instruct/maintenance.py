MOD = 10**9 + 7

def min_cost(prime_factors):
    from collections import Counter
    
    # Parse the input string into prime factors
    primes = []
    for i in range(0, len(prime_factors), 2):
        primes.append(int(prime_factors[i:i+2]))
    
    # Count the frequency of each prime factor
    prime_counts = Counter(primes)
    
    # Calculate the minimum cost
    min_cost = float('inf')
    total_K = 1
    for prime, count in prime_counts.items():
        total_K *= (prime ** count)
        current_cost = (count + 1) * prime
        if current_cost < min_cost:
            min_cost = current_cost
    
    # Return the minimum cost modulo 10^9 + 7
    return min_cost % MOD

# Read input
input_str = input().strip()

# Calculate and print the result
print(min_cost(input_str))
# Generator time: 28.4961 seconds