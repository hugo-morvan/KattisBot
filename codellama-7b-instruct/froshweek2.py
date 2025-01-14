import sys

def binary_search(target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if target == task[mid] or target == task[mid+1]:
        return mid
    elif target < task[mid]:
        return binary_search(target, start, mid-1)
    else:
        return binary_search(target, mid+1, end)

def solve():
    n, m = map(int, input().split())
    t = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    start_times = []
    end_times = []
    
    for i in range(n):
        start_times.append(l[0] + t[i])
        end_times.append(l[-1] - t[i])
        
    start_times.sort()
    end_times.sort()
    
    count = 0
    i = 0
    j = 0
    
    while i < n and j < m:
        if start_times[i] <= l[j+1]:
            count += 1
            i += 1
        elif end_times[i-1] >= l[j]:
            j += 1
            
    return binary_search(max(start_times) + max(t), 0, n-1)
        
print(solve())
# Generator time: 22.2487 seconds