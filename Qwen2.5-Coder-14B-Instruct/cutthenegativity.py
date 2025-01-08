n = int(input())
flights = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != -1:
            flights.append((i + 1, j + 1, row[j]))

flights.sort()

print(len(flights))
for u, v, c in flights:
    print(u, v, c)
# Generator time: 13.6161 seconds