n = int(input())

# Step 1: Identify the strongest athlete
strongest = None
for i in range(1, n+1):
    for j in range(i+1, n+1):
        min_time = query(i, j)
        if strongest is None or min_time > query(strongest[0], strongest[1]):
            strongest = (i, j)

# Step 2: Determine the imperturbability of all athletes except one
estimated_times = [None] * (n+1)
for i in range(1, n+1):
    if i == strongest[0]:
        estimated_times[i] = query(strongest[1], i) - 1
    elif i == strongest[1]:
        estimated_times[i] = query(strongest[0], i) - 1
    else:
        for j in range(1, n+1):
            if j != i and j != strongest[0] and j != strongest[1]:
                min_time = query(i, j)
                if estimated_times[j] is None or min_time < estimated_times[j]:
                    estimated_times[i] = min_time
                    break

# Step 3: Output the results
print(f"! {' '.join(map(str, estimated_times))}")
# Generator time: 10.7554 seconds