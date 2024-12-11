N = int(input())
preferences = []

for _ in range(N):
    a, b = map(int, input().split())
    preferences.append((a, b))

preferences.sort()

max_temp = preferences[0][1]
min_temp = preferences[-1][0]

if max_temp < min_temp:
    print("bad news")
else:
    count = max_temp - min_temp + 1
    print(count, min_temp)