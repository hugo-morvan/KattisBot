import sys

def main():
    N = int(input())
    for _ in range(N):
        cost = int(input())
        digit_count = len(str(cost))
        print(digit_count)

if __name__ == "__main__":
    sys.exit(main())