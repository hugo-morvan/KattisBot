def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_min_max(L, D, X):
    min_N = None
    max_M = None
    
    for num in range(L, D + 1):
        if sum_of_digits(num) == X:
            if min_N is None or num < min_N:
                min_N = num
            if max_M is None or num > max_M:
                max_M = num
                
    return min_N, max_M

# Read input
L = int(input())
D = int(input())
X = int(input())

# Find and print the result
min_N, max_M = find_min_max(L, D, X)
print(min_N)
print(max_M)