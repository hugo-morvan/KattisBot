def max_tasks(n, m, task_times, quiet_intervals):
    # Sort both lists to try to fit the smallest tasks into the smallest intervals
    task_times.sort()
    quiet_intervals.sort()
    
    task_index = 0
    interval_index = 0
    completed_tasks = 0
    
    while task_index < n and interval_index < m:
        if task_times[task_index] <= quiet_intervals[interval_index]:
            # If the current task can fit in the current interval, complete it
            completed_tasks += 1
            task_index += 1
        # Move to the next interval regardless of whether the task was completed or not
        interval_index += 1
    
    return completed_tasks

# Read input
n, m = map(int, input().split())
task_times = list(map(int, input().split()))
quiet_intervals = list(map(int, input().split()))

# Calculate and print the result
print(max_tasks(n, m, task_times, quiet_intervals))
# Generator time: 28.8993 seconds