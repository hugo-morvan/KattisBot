def count_completed_tasks(n, T, tasks):
    total_time = 0
    completed_count = 0
    
    for task_time in tasks:
        total_time += task_time
        if total_time > T:
            break
        completed_count += 1
    
    return completed_count

# Read input
n, T = map(int, input().split())
tasks = list(map(int, input().split()))

# Calculate and print the result
result = count_completed_tasks(n, T, tasks)
print(result)