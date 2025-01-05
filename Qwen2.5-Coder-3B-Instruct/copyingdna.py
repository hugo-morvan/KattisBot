def min_copy_operations(S, T):
    m, n = len(S), len(T)
    
    # Initialize the DP table
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            
            # Try all possible substrings of S
            for k in range(i):
                # Check if the substring S[k:i] can be reversed to match T[j-k:j]
                reversed_substring = S[k:i][::-1]
                if reversed_substring == T[j - k:j]:
                    dp[i][j] = min(dp[i][j], dp[k][j - k] + 1)
    
    # Determine if it is possible to transform S into T
    if dp[m][n] == float('inf'):
        return "impossible"
    else:
        return dp[m][n]

# Read input
t = int(input())
for _ in range(t):
    S = input()
    T = input()
    result = min_copy_operations(S, T)
    print(result)
# Generator time: 33.3798 seconds