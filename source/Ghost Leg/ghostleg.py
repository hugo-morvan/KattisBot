def ghost_leg_permutation(n, m, rungs):
    # Initialize the permutation list with numbers from 1 to n
    permutation = list(range(1, n + 1))
    
    # Process each rung to update the permutation
    for i in range(m):
        a = rungs[i]
        # Find the current position of element a
        current_pos = permutation.index(a)
        # Swap element a with the element directly below it
        permutation[current_pos], permutation[current_pos + 1] = permutation[current_pos + 1], permutation[current_pos]
    
    # Print the resulting permutation
    for element in permutation:
        print(element)

# Read input
n, m = map(int, input().split())
rungs = [int(input()) for _ in range(m)]

# Call the function with the input values
ghost_leg_permutation(n, m, rungs)