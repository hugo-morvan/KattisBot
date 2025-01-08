import sys
from collections import defaultdict, deque

# Read input
input = sys.stdin.read
data = input().split()

N = int(data[0])
s = int(data[1])

jobs = []
for i in range(N):
    x_i = int(data[2 + 2 * i])
    p_i = int(data[3 + 2 * i])
    jobs.append((x_i, p_i))

# Build the graph and calculate in-degrees
graph = defaultdict(list)
in_degree = [0] * N
for i, (x_i, p_i) in enumerate(jobs):
    if p_i != 0:
        graph[p_i - 1].append(i)

# Initialize the queue for topological sort
queue = deque()
for i in range(N):
    if in_degree[i] == 0:
        queue.append(i)

# Perform topological sort and calculate maximum profit
max_profit = s
while queue:
    node = queue.popleft()
    current_profit = max_profit + jobs[node][0]
    
    # Update the profit for dependent jobs
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)
        
        # Calculate the maximum profit for each possible order of dependent jobs
        max_profit_for_dependency = max(current_profit, max_profit_for_dependency)
    
    # Update the current maximum profit
    max_profit = max(max_profit, current_profit)

print(max_profit - s)
# Generator time: 10.4986 seconds