def min_mutations(N, dna):
    # Count the number of 'B' characters in the DNA string
    B_count = dna.count('B')
    
    # Calculate the minimum number of mutations needed
    # We can either flip all 'B's to 'A's or flip the prefix and then handle any remaining 'B's
    # The optimal strategy is to flip the prefix that covers the maximum number of 'B's
    max_B_in_prefix = 0
    current_B_count = 0
    
    for i in range(N):
        if dna[i] == 'B':
            current_B_count += 1
        else:
            max_B_in_prefix = max(max_B_in_prefix, current_B_count)
            current_B_count = 0
    
    # Consider the case where the last segment is all 'B's
    max_B_in_prefix = max(max_B_in_prefix, current_B_count)
    
    # The minimum mutations will be the smaller of:
    # 1. Flipping all 'B's to 'A's
    # 2. Flipping the prefix that covers the maximum number of 'B's and then handling any remaining 'B's
    return min(B_count, N - max_B_in_prefix)

# Read input
N = int(input())
dna = input().strip()

# Calculate and print the result
print(min_mutations(N, dna))
# Generator time: 37.3996 seconds