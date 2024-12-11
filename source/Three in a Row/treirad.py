def count_triple_numbers(N):
    count = 0
    for a in range(1, N):
        b = a + 1
        c = a + 2
        product = a * b * c
        if product < N:
            count += 1
    return count

# Read input
N = int(input())

# Calculate and print the result
print(count_triple_numbers(N))