def min_copy_operations(S, T):
    m, n = len(S), len(T)
    
    # dp[i][j] will store the minimum number of copy operations needed to create T[:i] from S[:j]
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Try copying from S
            for k in range(j):
                if T[i-1::-1].startswith(S[k:j]):
                    dp[i][j] = min(dp[i][j], dp[i-j+k][k] + 1)
            
            # Try copying from partial T
            for k in range(i):
                if T[:i].startswith(T[k:i][::-1]):
                    dp[i][j] = min(dp[i][j], dp[k][j] + 1)
    
    result = dp[n][m]
    return result if result != float('inf') else "impossible"

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        S = input().strip()
        T = input().strip()
        result = min_copy_operations(S, T)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 40.2245 seconds