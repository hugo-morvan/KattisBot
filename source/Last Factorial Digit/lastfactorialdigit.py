def last_digit_of_factorial(n):
    if n == 0 or n == 1:
        return 1
    if n >= 5:
        return 0
    result = 1
    for i in range(2, n + 1):
        result *= i
        result %= 10
    return result

def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(last_digit_of_factorial(N))

if __name__ == "__main__":
    main()