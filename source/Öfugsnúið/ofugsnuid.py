n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.reverse()
print(*numbers)