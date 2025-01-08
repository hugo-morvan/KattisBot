def calculate_average_rank(n, w):
    points = [0] * (n + 1)
    ranks = [0] * (n + 1)
    
    for _ in range(w):
        k = int(input())
        winners = list(map(int, input().split()))
        for competitor in winners:
            points[competitor] += 1
    
    rank = n
    for i in range(n, 0, -1):
        while rank > 0 and sum(1 for p in points if p >= rank) == sum(1 for p in points if p > rank):
            rank -= 1
        for competitor in range(1, n + 1):
            if points[competitor] == rank:
                ranks[competitor] = rank
    
    for i in range(1, n + 1):
        print(ranks[i])

# Read input
n, w = map(int, input().split())

calculate_average_rank(n, w)
# Generator time: 7.3457 seconds