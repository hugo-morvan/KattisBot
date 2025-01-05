import sys
from collections import defaultdict

def max_profit(N, s, jobs):
    # Read input data
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    
    for i in range(1, N + 1):
        profit, prev_job = map(int, input().split())
        graph[prev_job].append(i)
        in_degree[i] += 1
    
    # Initialize the queue with jobs that have no dependencies
    queue = [i for i in range(1, N + 1) if in_degree[i] == 0]
    dp = [0] * (N + 1)
    
    # Perform topological sorting
    while queue:
        job = queue.pop(0)
        for next_job in graph[job]:
            dp[next_job] = max(dp[next_job], dp[job] + jobs[next_job])
            in_degree[next_job] -= 1
            if in_degree[next_job] == 0:
                queue.append(next_job)
    
    # Calculate the maximum profit considering the initial amount of money
    max_profit = max(dp[i] for i in range(1, N + 1))
    return max_profit - s

# Read input
N, s = map(int, input().split())
jobs = list(map(int, input().split()))

# Calculate and print the maximum profit
print(max_profit(N, s, jobs))
# Generator time: 24.5932 seconds