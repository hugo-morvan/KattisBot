N = int(input())
days = input().split()
hungover_days = 0

for i in range(1, N - 1):
    if days[i] == "drunk":
        hungover_days += 1

print(hungover_days)