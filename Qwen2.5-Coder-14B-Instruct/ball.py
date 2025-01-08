n = int(input())
from collections import defaultdict

# Dictionary to count occurrences of each student
count = defaultdict(int)

# Read all pairs and count occurrences
for _ in range(n // 2 + 1):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1

# Find the pair that appears an odd number of times
extra_pair = []
for student, cnt in count.items():
    if cnt % 2 == 1:
        extra_pair.append(student)

# Ensure the output is sorted and printed on a single line
extra_pair.sort()
print(extra_pair[0], extra_pair[1])
# Generator time: 19.4505 seconds