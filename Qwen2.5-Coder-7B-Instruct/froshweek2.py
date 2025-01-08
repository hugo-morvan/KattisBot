def max_tasks(n, m, task_times, quiet_intervals):
    # Sort the task times and quiet intervals in ascending order
    task_times.sort()
    quiet_intervals.sort()

    i = j = 0
    completed_tasks = 0

    # Iterate through both lists to count how many tasks can be completed
    while i < n and j < m:
        if task_times[i] <= quiet_intervals[j]:
            # If the current task fits within the current quiet interval, complete it
            i += 1
            completed_tasks += 1
        else:
            # Move to the next quiet interval since the current one is too short for the task
            j += 1

    return completed_tasks

# Read input from user
n, m = map(int, input().split())
task_times = list(map(int, input().split()))
quiet_intervals = list(map(int, input().split()))

# Calculate and print the maximum number of tasks Zac can complete
print(max_tasks(n, m, task_times, quiet_intervals))
# Generator time: 7.7139 seconds