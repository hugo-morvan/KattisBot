import sys
import math

def expected_hearings(n, hearings):
    # Sort hearings by start time
    hearings.sort(key=lambda x: x[0])
    
    # Initialize DP table
    dp = [0] * (n + 1)
    
    # Fill DP table
    for i in range(1, n + 1):
        start_time, min_length, max_length = hearings[i - 1]
        dp[i] = dp[i - 1] + 1
        
        # Try skipping the current hearing and starting the next one
        if i > 1:
            dp[i] = max(dp[i], dp[i - 2] + 1)
        
        # Try attending the current hearing
        if start_time + min_length <= hearings[i - 1][0]:
            dp[i] = max(dp[i], dp[i - 1] + 1)
    
    return dp[n]

# Read input
n = int(sys.stdin.readline().strip())
hearings = []
for _ in range(n):
    s, a, b = map(int, sys.stdin.readline().strip().split())
    hearings.append((s, a, b))

# Calculate expected number of hearings
expected_value = expected_hearings(n, hearings)

# Print the result
print(expected_value)
# Generator time: 15.2904 seconds