def max_tasks(n, m, t, l):
    # Sort task durations and quiet interval lengths
    t.sort()
    l.sort()
    
    # Initialize dp array to store the maximum tasks that can be completed up to each interval
    dp = [0] * (m + 1)
    
    # Iterate through each quiet interval
    for i in range(m):
        # Try to fit as many tasks as possible into the current interval
        for j in range(n):
            if t[j] <= l[i]:
                dp[i + 1] = max(dp[i + 1], dp[i] + 1)
            else:
                break
    
    # The result is the maximum value in the dp array
    return dp[m]

# Read input
n, m = map(int, input().split())
t = list(map(int, input().split()))
l = list(map(int, input().split()))

# Compute and print the result
print(max_tasks(n, m, t, l))
# Generator time: 22.3138 seconds