def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_smallest_p(N):
    for p in range(11, 100001):
        if digit_sum(N * p) == digit_sum(N):
            return p

while True:
    N = int(input())
    if N == 0:
        break
    p = find_smallest_p(N)
    print(p)