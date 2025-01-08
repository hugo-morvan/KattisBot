import math

def calculate_probability(m, n, t, p):
    total_combinations = math.comb(m, n)
    favorable_combinations = 0
    
    for i in range(p + 1):
        if (n - i) * t >= p:
            favorable_combinations += math.comb(n, i) * math.comb(m - n, n - i)
    
    probability = favorable_combinations / total_combinations
    return probability

# Read input
m, n, t, p = map(int, input().split())

# Calculate and print the probability
result = calculate_probability(m, n, t, p)
print(f"{result:.10f}")
# Generator time: 5.9350 seconds