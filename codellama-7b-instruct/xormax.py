n = int(input())
arr = [int(i) for i in input().split(' ')]
max_value = 0
for i in range(n):
	for j in range(i+1, n):
		if arr[i]^arr[j] > max_value:
			max_value = arr[i] ^ arr[j]
print(max_value)
# Generator time: 14.0041 seconds