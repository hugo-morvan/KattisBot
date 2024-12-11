def calculate_probability(N, A):
    # Initialize a dictionary to count occurrences of each sum
    sum_counts = {i: 0 for i in range(2, 13)}
    
    # Count occurrences of each sum
    for i in range(1, 7):
        for j in range(1, 7):
            sum_counts[i + j] += 1
    
    # Calculate the probability for each distance
    probability = sum(sum_counts[a] / 36 for a in A)
    
    # Return the probability rounded to 4 decimal places
    return round(probability, 4)

# Read input
N = int(input())
A = list(map(int, input().split()))

# Calculate and print the probability
print(calculate_probability(N, A))