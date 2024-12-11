def check_odd_or_even():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Iterate over each test case
    for _ in range(num_test_cases):
        # Read the integer from input
        x = int(input())
        
        # Check if the number is odd or even
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")

# Call the function to execute the program
check_odd_or_even()