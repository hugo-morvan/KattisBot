def farey_sequence_length(N):
    if N == 1:
        return 2
    result = 0
    for i in range(1, N + 1):
        result += (N // i) * phi(i)
    return result + 1

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        length = farey_sequence_length(N)
        print(K, length)

if __name__ == "__main__":
    main()
# Generator time: 24.9409 seconds