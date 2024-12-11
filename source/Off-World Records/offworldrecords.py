# Read input
n, c, p = map(int, input().split())
high_jumps = [int(input()) for _ in range(n)]

# Initialize counters
new_records = 0
current_record = p

# Iterate through high jump heights
for height in high_jumps:
    if height > current_record + p:
        new_records += 1
        current_record = height

# Output the result
print(new_records)