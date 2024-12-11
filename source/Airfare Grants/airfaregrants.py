N = int(input())
prices = sorted([int(input()) for _ in range(N)], reverse=True)
min_cost = min(prices[0], prices[N-1] // 2)
print(min_cost)