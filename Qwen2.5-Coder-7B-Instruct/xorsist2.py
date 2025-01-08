def xor_from_1_to_n(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def xor_between_a_and_b(a, b):
    xor_1_to_a_minus_one = xor_from_1_to_n(a - 1)
    xor_1_to_b = xor_from_1_to_n(b)
    return xor_1_to_a_minus_one ^ xor_1_to_b

def solve_gunnar_problem():
    N = int(input())
    a, b = map(int, input().split())
    
    result = xor_between_a_and_b(a, b)
    
    if result == 0:
        print("Enginn")
    elif result > N:
        print("Gunnar")
    else:
        print(result)

# Run the function to solve the problem
solve_gunnar_problem()
# Generator time: 9.2284 seconds