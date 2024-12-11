n = int(input())
excluded_count = 0

for _ in range(n):
    difficulty = int(input())
    if difficulty % 2 != 0:
        excluded_count += 1

print(excluded_count)