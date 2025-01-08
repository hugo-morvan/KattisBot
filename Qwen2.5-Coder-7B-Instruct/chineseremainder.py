from math import gcd

def find_solution(T):
    results = []
    for _ in range(T):
        a, n, b, m = map(int, input().split())
        K = n * m
        if (b - a) % gcd(n, m) == 0:
            x = a + ((b - a) // gcd(n, m)) * n
            results.append((x % K, K))
        else:
            results.append((-1, K))  # No solution if gcd condition is not met
    
    for result in results:
        print(result[0], result[1])

# Read the number of test cases
T = int(input())
find_solution(T)
# Generator time: 6.3420 seconds