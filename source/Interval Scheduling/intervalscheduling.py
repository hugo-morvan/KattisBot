def max_nonoverlapping_intervals():
    n = int(input())
    intervals = []
    
    for _ in range(n):
        s, f = map(int, input().split())
        intervals.append((s, f))
    
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end_time = -1
    
    for start, end in intervals:
        if start >= end_time:
            count += 1
            end_time = end
    
    print(count)

max_nonoverlapping_intervals()