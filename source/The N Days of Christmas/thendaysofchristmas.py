def calculate_gifts(N):
    # Calculate the number of gifts on the N-th day
    gifts_on_nth_day = sum(range(1, N + 1))
    
    # Calculate the total number of gifts received by the end of the N-th day
    total_gifts = sum(sum(range(1, i + 1)) for i in range(1, N + 1))
    
    return gifts_on_nth_day, total_gifts

# Read input
N = int(input())

# Calculate and print the results
gifts_on_nth_day, total_gifts = calculate_gifts(N)
print(gifts_on_nth_day)
print(total_gifts)