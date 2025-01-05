def count_valid_binary_strings(n):
    MOD = 10**9 + 7
    
    # Base cases
    if n == 1:
        return 2  # "0" and "1"
    if n == 2:
        return 3  # "00", "01", "10"
    
    # Initialize dp array
    dp = [0] * (n + 1)
    dp[1], dp[2] = 2, 3
    
    # Fill dp array using the transitions
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[n]

# Read input
T = int(input())
for _ in range(T):
    n = int(input())
    result = count_valid_binary_strings(n)
    print(result)
# Generator time: 23.9022 seconds