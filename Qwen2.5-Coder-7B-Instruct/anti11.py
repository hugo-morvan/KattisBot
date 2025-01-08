MOD = 10**9 + 7

def count_binary_strings(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    # dp[i] will store the number of valid binary strings of length i
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n + 1):
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
# Generator time: 8.8626 seconds