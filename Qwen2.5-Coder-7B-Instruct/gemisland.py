import numpy as np

def expected_gems(n, d, r):
    # Initialize a DP table where dp[i][j] is the expected number of gems held by the top j inhabitants after i nights
    dp = np.zeros((d + 1, n + 1))
    
    # Base case: After 0 nights, each inhabitant has 1 gem
    for i in range(n):
        dp[0][i] = 1
    
    # Fill the DP table
    for night in range(1, d + 1):
        for inhabitants in range(1, n + 1):
            total_gems = inhabitants * (inhabitants + 1) / 2
            expected_value = 0
            
            # Calculate the expected value of the top r inhabitants
            if r <= inhabitants:
                for k in range(r):
                    expected_value += dp[night - 1][k] * (inhabitants - k)
                
                expected_value /= r
    
            dp[night][inhabitants] = expected_value
    
    # Return the expected number of gems held by the top r inhabitants after d nights
    return dp[d][r]

# Read input
n, d, r = map(int, input().split())

# Calculate and print the result
result = expected_gems(n, d, r)
print(f"{result:.6f}")
# Generator time: 16.6827 seconds