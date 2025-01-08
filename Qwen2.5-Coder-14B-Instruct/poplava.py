def find_histogram(N, X):
    if X == 0:
        return list(range(1, N + 1))
    
    if N % 2 == 0 and (X - N) % 2 == 0:
        h = [i for i in range(1, N + 1)]
        for i in range(N // 2):
            h[i] += (X - N) // 2
            h[N - i - 1] -= (X - N) // 2
        return h
    
    if N % 2 == 1 and X % 2 == 0:
        h = [i for i in range(1, N + 1)]
        for i in range(N // 2):
            h[i] += X // 2
            h[N - i - 1] -= X // 2
        return h
    
    return -1

N, X = map(int, input().split())
result = find_histogram(N, X)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))
# Generator time: 31.8191 seconds