import sys

# Read input
n = int(input())
k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Function to find the median of a list
def median(lst):
    lst.sort()
    mid = len(lst) // 2
    if len(lst) % 2 == 1:
        return lst[mid]
    else:
        return (lst[mid - 1] + lst[mid]) / 2

# Generate the plan
plan = []
for i in range(n):
    choices = [k[i], a[i], b[i]]
    plan.append(median(choices))

# Print the plan
print(*plan)