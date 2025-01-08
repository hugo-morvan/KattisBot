import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])

difficulties = list(map(int, data[2:N+2]))
queries = [(int(data[N+2+i]), int(data[N+3+i])) for i in range(Q)]

# Sort the difficulties to easily find and discard
difficulties.sort()

# Function to binary search and find the index of the first difficulty greater than D
def bisect_right(arr, D):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > D:
            right = mid
        else:
            left = mid + 1
    return left

# Function to binary search and find the index of the last difficulty less than or equal to D
def bisect_left(arr, D):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= D:
            left = mid + 1
        else:
            right = mid
    return left - 1

results = []
for T, D in queries:
    if T == 1:  # Discard problems strictly harder than D
        idx = bisect_right(difficulties, D)
        if idx < len(difficulties):
            results.append(str(difficulties[idx]))
            difficulties.pop(idx)
        else:
            results.append("-1")
    elif T == 2:  # Discard the hardest problem not harder than D
        idx = bisect_left(difficulties, D)
        if idx >= 0:
            results.append(str(difficulties[idx]))
            difficulties.pop(idx)
        else:
            results.append("-1")

for result in results:
    print(result)
# Generator time: 12.4697 seconds