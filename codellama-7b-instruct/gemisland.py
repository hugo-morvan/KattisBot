n = int(input())
d = int(input())
r = int(input())

# Calculate the total number of gems after d nights.
total_gems = 0
for i in range(1, n + 1):
    total_gems += i ** d

# Calculate the number of gems for each inhabitant and sort them.
inhabitants = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    inhabitants[i] = [i ** d, i]
for inhabitant in sorted(inhabitants, key=lambda x: x[0], reverse=True):
    print("{:.6f}".format(inhabitant[1]))
# Generator time: 6.0519 seconds