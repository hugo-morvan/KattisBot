# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the number of power strips and their respective outlets
    K = int(input())
    outlets = list(map(int, input().split()))
    
    # Initialize the total number of appliances that can be powered
    max_appliances = 1
    
    # Calculate the maximum number of appliances that can be powered
    for out in outlets:
        if out > 1:
            max_appliances *= out
    
    # Print the result
    print(max_appliances)