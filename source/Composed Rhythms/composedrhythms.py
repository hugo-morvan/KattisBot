
n = int(input())
groups = []
remaining = n

while remaining > 0:
    if remaining >= 3:
        groups.append(3)
        remaining -= 3
    else:
        groups.append(2)
        remaining -= 2

print(len(groups))
print(*groups)
