def count_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    # Initialize a list to store the number of ways to make each length up to n
    ways = [0] * (n + 1)
    
    # Base case: there's one way to make a plank of length 0
    ways[0] = 1
    
    # Fill the array with the number of ways to make each length
    for i in range(1, n + 1):
        if i >= 1:
            ways[i] += ways[i - 1]
        if i >= 2:
            ways[i] += ways[i - 2]
        if i >= 3:
            ways[i] += ways[i - 3]
    
    return ways[n]

# Read input
n = int(input())

# Output the result
print(count_ways(n))