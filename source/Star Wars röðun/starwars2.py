def starwars_order(n):
    # Read the input
    numbers = list(map(int, input().split()))
    
    # Split the list into three parts
    first_third = numbers[:n//3]
    middle_third = numbers[n//3:n//3*2]
    last_third = numbers[n//3*2:]
    
    # Rearrange the list according to starwars-order
    rearranged = middle_third + first_third + last_third
    
    # Print the rearranged list
    print(' '.join(map(str, rearranged)))

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    starwars_order(int(input()))