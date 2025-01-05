import sys

def solve():
    T = int(input())
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        # If N is odd, the light will be on after K snaps
        if N % 2 == 1:
            print(f"Case #{t}: ON")
        else:
            # If N is even, the light will be off after K snaps
            print(f"Case #{t}: OFF")

if __name__ == "__main__":
    solve()
# Generator time: 5.7208 seconds