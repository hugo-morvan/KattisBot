def can_win(n):
    return n % 2 == 1

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    piles = list(map(int, input().split()))
    
    if can_win(n):
        results.append(1)
    else:
        results.append(0)

for result in results:
    print(result)
# Generator time: 4.3103 seconds