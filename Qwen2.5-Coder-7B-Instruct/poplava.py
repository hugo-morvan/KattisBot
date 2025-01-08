def find_histogram(N, X):
    if N == 1:
        return [X] if X == 1 else -1
    
    # Calculate the minimum possible height sum for a valid histogram
    min_height_sum = (N * (N + 1)) // 2
    
    # Check if X is within the range of possible sums
    if X < min_height_sum or X > N * N:
        return -1
    
    # Construct a histogram with heights that sum up to exactly X
    histogram = []
    current_sum = 0
    
    for i in range(N):
        if current_sum + (N - i) <= X:
            height = N - i
        else:
            height = X - current_sum
        histogram.append(height)
        current_sum += height
    
    return histogram

# Input reading
N, X = map(int, input().split())

# Find and print the result
result = find_histogram(N, X)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))
# Generator time: 7.8466 seconds