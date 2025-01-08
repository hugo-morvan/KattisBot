def max_profit(N, s, jobs):
    # Sort jobs based on their dependency
    jobs.sort(key=lambda x: x[1])
    
    # Initialize a DP array where dp[i] is the maximum profit ending with job i
    dp = [float('-inf')] * (N + 1)
    
    # Base case: If you don't take any job, your profit is 0
    dp[0] = s
    
    for i in range(1, N + 1):
        x_i, p_i = jobs[i - 1]
        
        # Calculate the maximum profit if we take the i-th job
        if p_i == 0:
            dp[i] = max(dp[i], dp[0] + x_i)
        else:
            dp[i] = max(dp[i], dp[p_i] + x_i)
        
        # Update dp[j] for all jobs j that depend on i
        for j in range(i + 1, N + 1):
            if jobs[j - 1][1] == i:
                dp[j] = max(dp[j], dp[i])
    
    # The maximum profit is the maximum value in dp array minus the initial amount of money s
    return max(max(dp) - s, 0)

# Read input
N, s = map(int, input().split())
jobs = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(max_profit(N, s, jobs))
# Generator time: 42.2548 seconds