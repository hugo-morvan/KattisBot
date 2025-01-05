from math import gcd

def farey_sequence_length(N):
    count = 1  # Start with 0/1
    a, b = 0, 1
    while True:
        next_a = a + b
        next_b = b
        if next_b > N:
            break
        if gcd(next_a, next_b) == 1:
            count += 1
        a, b = next_a, next_b
    return count

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        length = farey_sequence_length(N)
        print(f"{K} {length}")

if __name__ == "__main__":
    main()
# Generator time: 18.7293 seconds