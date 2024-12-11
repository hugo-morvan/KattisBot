import math

def check_number(N):
    if N % 2 == 1:
        return "O"
    elif math.isqrt(N) ** 2 == N:
        return "S"
    elif math.isqrt(N) ** 2 == N and N % 2 == 1:
        return "OS"
    else:
        return "EMPTY"

T = int(input())
for _ in range(T):
    N = int(input())
    result = check_number(N)
    print(result)