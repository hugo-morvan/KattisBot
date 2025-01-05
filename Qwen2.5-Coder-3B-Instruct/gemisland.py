import numpy as np

def expected_top_r_gems(n, d, r):
    # Initialize the number of gems for each inhabitant
    gems = np.ones(n)
    
    # Simulate the gem splitting process for d nights
    for _ in range(d):
        # Randomly select one gem to split
        index_to_split = np.random.randint(n)
        gems[index_to_split] *= 2
    
    # Sort the gems in non-increasing order
    gems_sorted = np.sort(gems)[::-1]
    
    # Calculate the expected sum of the top r gems
    expected_sum = np.sum(gems_sorted[:r])
    
    return expected_sum

# Read input
n, d, r = map(int, input().split())

# Calculate the expected number of gems
result = expected_top_r_gems(n, d, r)

# Print the result
print(result)
# Generator time: 23.7371 seconds