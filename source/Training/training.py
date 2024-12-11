import sys

# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
s = int(data[1])

problems = []
for i in range(2, len(data), 2):
    l = int(data[i])
    r = int(data[i + 1])
    problems.append((l, r))

# Sort problems by upper bound
problems.sort(key=lambda x: x[1])

# Initialize max_skill_level
max_skill_level = s

# Iterate through problems
for l, r in problems:
    if s >= l:
        max_skill_level += 1
        s += 1
    else:
        break

# Output the result
print(max_skill_level)