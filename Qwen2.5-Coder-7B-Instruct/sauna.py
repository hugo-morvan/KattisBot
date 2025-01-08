def find_suitable_temperatures():
    N = int(input())
    preferences = []
    
    for _ in range(N):
        a_i, b_i = map(int, input().split())
        preferences.append((a_i, b_i))
    
    # Find the intersection of all temperature ranges
    min_temp = max(a_i for a_i, b_i in preferences)
    max_temp = min(b_i for a_i, b_i in preferences)
    
    if min_temp > max_temp:
        print("bad news")
    else:
        suitable_temperatures = max_temp - min_temp + 1
        print(suitable_temperatures, min_temp)

find_suitable_temperatures()
# Generator time: 6.4165 seconds