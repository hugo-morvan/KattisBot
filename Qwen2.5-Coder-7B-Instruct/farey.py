from math import gcd

def farey_sequence_length(N):
    length = 0
    for b in range(1, N + 1):
        for a in range(b // (b // 2), b + 1):
            if gcd(a, b) == 1:
                length += 1
    return length

def main():
    P = int(input())
    for K in range(1, P + 1):
        N = int(input())
        result = farey_sequence_length(N)
        print(f"{K} {result}")

if __name__ == "__main__":
    main()
# Generator time: 5.5272 seconds