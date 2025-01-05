# Read input values
N = int(input())
a, b = map(int, input().split())

# Calculate XOR of numbers from a to b
result = 0
for i in range(a, b + 1):
    result ^= i

# Determine the output based on the result
if result == 0:
    print("Enginn")
elif result <= N:
    print(result)
else:
    print("Gunnar")
# Generator time: 4.7168 seconds