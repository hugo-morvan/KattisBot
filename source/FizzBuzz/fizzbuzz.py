def fizz_buzz(x, y, n):
    for i in range(1, n + 1):
        if i % (x * y) == 0:
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)

# Read input
X, Y, N = map(int, input().split())

# Call the function
fizz_buzz(X, Y, N)