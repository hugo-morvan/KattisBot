while True:
    try:
        n = int(input())
        print(n * (n + 1) // 2)
    except EOFError:
        break
# Generator time: 6.9139 seconds