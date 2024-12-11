def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = 2 ** (k + 1) - 1
        print(n)

if __name__ == "__main__":
    main()