def min_copy_operations(S, T):
    m = len(S)
    n = len(T)
    
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0]
    
    for j in range(1, n + 1):
        dp[0][j] = float('inf')
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            
            # Copy from S
            for k in range(j, -1, -1):
                dp[i][j] = min(dp[i][j], dp[i-k][k] + (dp[i-k][k] != 0))
            
            # Reverse and copy from S
            for k in range(j, -1, -1):
                rev_S = S[k-1:i][::-1]
                if T[j-1] == rev_S[-1]:
                    dp[i][j] = min(dp[i][j], dp[i-k][k] + (dp[i-k][k] != 0))
    
    result = dp[m][n]
    return result if result < float('inf') else "impossible"

def main():
    t = int(input())
    for _ in range(t):
        S = input().strip()
        T = input().strip()
        print(min_copy_operations(S, T))

if __name__ == "__main__":
    main()
# Generator time: 11.3240 seconds