import math

def calculate_probability(m, n, t, p):
    # Calculate the binomial coefficient
    def binom(n, k):
        return math.comb(n, k)
    
    # Total number of ways to choose n winners out of m
    total_ways = binom(m, n)
    
    # Number of favorable outcomes where all p people are among the n winners
    favorable_ways = binom(p, p) * binom(m - p, n - p)
    
    # Calculate the probability
    probability = favorable_ways / total_ways
    
    return probability

# Read input
m, n, t, p = map(int, input().split())

# Calculate and print the probability
probability = calculate_probability(m, n, t, p)
print(probability)
# Generator time: 23.3455 seconds