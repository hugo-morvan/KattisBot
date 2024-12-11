n = int(input())
temperatures = list(map(int, input().split()))

highest_temp = max(temperatures)
lowest_temp = min(temperatures)

print(highest_temp, lowest_temp)