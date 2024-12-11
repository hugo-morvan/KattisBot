def zoom_out(n, k):
    # Read the list of numbers
    numbers = list(map(int, input().split()))
    
    # Calculate the number of elements to keep
    q = n // k
    
    # Extract every k-th element starting from the 1st element
    result = [numbers[i] for i in range(0, q * k, k)]
    
    # Print the result
    print(' '.join(map(str, result)))

# Read the input values
n, k = map(int, input().split())
zoom_out(n, k)