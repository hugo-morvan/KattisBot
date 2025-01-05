import math

def solve_modular_equations():
    T = int(input())
    for _ in range(T):
        a, n, b, m = map(int, input().split())
        
        # Calculate the modular inverse of n modulo m
        inv_n = pow(n, -1, m)
        
        # Calculate the solution x
        x = (a * m * inv_n + b) % (n * m)
        
        # Output the result
        print(x, n * m)

solve_modular_equations()
# Generator time: 5.1641 seconds