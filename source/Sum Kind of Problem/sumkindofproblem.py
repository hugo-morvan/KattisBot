# Read the number of data sets
P = int(input())

for _ in range(P):
    # Read the data set number and N
    K, N = map(int, input().split())
    
    # Calculate the sums
    S1 = N * (N + 1) // 2  # Sum of the first N positive integers
    S2 = N * N  # Sum of the first N odd integers
    S3 = N * (N + 1)  # Sum of the first N even integers
    
    # Print the result
    print(f"{K} {S1} {S2} {S3}")