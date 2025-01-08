def min_mutations(N, sequence):
    A_count = sequence.count('A')
    B_count = N - A_count
    
    # The minimum number of mutations is the maximum between the count of 'A's and 'B's
    return max(A_count, B_count)

# Read input
N = int(input())
sequence = input()

# Output the result
print(min_mutations(N, sequence))
# Generator time: 4.4420 seconds