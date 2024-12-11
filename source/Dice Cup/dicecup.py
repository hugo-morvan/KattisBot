def most_likely_outcomes(N, M):
    # Create a dictionary to store the frequency of each possible sum
    sum_frequency = {}
    
    # Calculate all possible sums and their frequencies
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            total_sum = i + j
            if total_sum in sum_frequency:
                sum_frequency[total_sum] += 1
            else:
                sum_frequency[total_sum] = 1
    
    # Find the maximum frequency
    max_frequency = max(sum_frequency.values())
    
    # Collect all sums with the maximum frequency
    most_likely_sums = [sum_val for sum_val, freq in sum_frequency.items() if freq == max_frequency]
    
    # Print the most likely outcomes
    for outcome in most_likely_sums:
        print(outcome)

# Read input
N, M = map(int, input().split())

# Compute and print the most likely outcomes
most_likely_outcomes(N, M)