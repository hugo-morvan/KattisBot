def find_common_temperatures():
    import sys
    
    N = int(input())
    min_temp = float('inf')
    max_temp = float('-inf')
    
    for _ in range(N):
        a, b = map(int, input().split())
        min_temp = max(min_temp, a)
        max_temp = min(max_temp, b)
    
    if min_temp > max_temp:
        print("bad news")
    else:
        num_options = max_temp - min_temp + 1
        lowest_temp = min_temp
        print(num_options, lowest_temp)

find_common_temperatures()
# Generator time: 17.7402 seconds