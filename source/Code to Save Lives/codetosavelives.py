def sum_numerically_distanced_numbers():
    # Read the number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read the first numerically distanced number
        num1 = input().split()
        num1 = [int(digit) for digit in num1]
        
        # Read the second numerically distanced number
        num2 = input().split()
        num2 = [int(digit) for digit in num2]
        
        # Calculate the sum of the two numbers
        result = []
        for i in range(len(num1)):
            result.append(num1[i] + num2[i])
        
        # Print the result as a space-separated string
        print(' '.join(map(str, result)))

sum_numerically_distanced_numbers()