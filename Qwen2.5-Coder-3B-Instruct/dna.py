def min_mutations(N, sequence):
    # Count the number of 'B's in the sequence
    num_Bs = sequence.count('B')
    
    # Initialize the minimum number of mutations to the number of 'B's
    min_mutations = num_Bs
    
    # Iterate over all possible prefixes
    for K in range(1, N + 1):
        # Calculate the number of 'A's after applying the prefix mutation
        remaining_As = N - K
        
        # Calculate the number of mutations needed for this prefix
        mutations = num_Bs - remaining_As
        
        # Update the minimum number of mutations
        min_mutations = min(min_mutations, mutations)
    
    return min_mutations

# Read input
N = int(input())
sequence = input()

# Output the result
print(min_mutations(N, sequence))
# Generator time: 21.6190 seconds