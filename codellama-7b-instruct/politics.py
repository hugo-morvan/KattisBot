n = int(input())
start_time = list()
min_length = list()
max_length = list()
for i in range(n):
    start, min_len, max_len = map(int, input().split())
    if not start_time or start > start_time[-1]:
        start_time.append(start)
        min_length.append(min_len)
        max_length.append(max_len)
    else:
        i = 0
        while i < n and start > start_time[i]:
            i += 1
        if i == n:
            continue
        else:
            start_time.insert(i, start)
            min_length.insert(i, min_len)
            max_length.insert(i, max_len)
n = len(start_time)
result = 0
for i in range(n-1):
    next_hearing_start_time = start_time[i+1]
    if not result:
        current_hearing_end_time = start_time[i] + max_length[i]
        result += 1
    else:
        while True:
            if next_hearing_start_time <= current_hearing_end_time:
                break
            else:
                current_hearing_end_time += min_length[i]
                result += 1
print(result)
# Generator time: 9.9648 seconds