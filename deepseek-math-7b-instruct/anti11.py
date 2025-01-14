 def solve(T):
    dp = [2] * (16) # For lengths less than or equal to 3 the only strings are "0", "1" and two possible strings of length 4, i.e., {00}, {"",""} which is not a valid input for this problem as it contains an invalid substring
    mod = int(1e9+7) # Modulo number used in output format (from required answer section above). This line can be removed after finding the recurrence relation and solving that. 
    
    def count_binaries():        for i in range(4, len(dp)+1):            dp[i] = ((dp[i-2]%mod) * 3 ) % mod # For a string of length "n", it can either end with '0', so the previous state is n - 1. Or ends with '1' and invalidates all states from i to len(s), thus making current valid only if last two elements are equal (i-2). This makes three choices: dp[max(0, i+3)] = ((dp[n]%mod) * mod ) % mod # The maximum allowed length is 16. It can be increased as per the problem constraints
    return [str((dp[x] - int("".join(["2" for _ in range(4 + x)], "")))%mod)]*T
# Generator time: 8.8003 seconds