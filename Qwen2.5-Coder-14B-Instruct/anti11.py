MOD = 10**9 + 7

def count_binary_strings(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    
    # Initialize the dp array
    dp = [0] * (n + 1)
    dp[1] = 2
    dp[2] = 3
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[n]

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        n = int(input())
        result = count_binary_strings(n)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 24.5248 seconds