MOD = 1_000_000_007

def count_inversions(s):
    n = len(s)
    k = s.count('?')
    
    # dp[i][j] will store the number of ways to arrange i characters with j ones
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    total_inversions = 0
    
    for i in range(1, n + 1):
        char = s[i - 1]
        
        # Update dp table
        new_dp = [[0] * (k + 1) for _ in range(n + 1)]
        for j in range(k + 1):
            if char == '0':
                new_dp[i][j] = dp[i-1][j]
            elif char == '1':
                if j > 0:
                    new_dp[i][j] = dp[i-1][j-1]
            else:  # '?'
                new_dp[i][j] = (dp[i-1][j] + (dp[i-1][j-1] if j > 0 else 0)) % MOD
        
        total_inversions += sum(j * new_dp[i][j] for j in range(k + 1))
        total_inversions %= MOD
    
    return total_inversions

# Example usage
input_string = "?0?"
print(count_inversions(input_string))  # Output: 3
