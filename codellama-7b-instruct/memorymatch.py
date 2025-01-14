def solve(cards):
    s = set()
    cnt = 0
    n = len(cards)
    for i in range(n -1):
        if cards[i] in s:
            return cnt + 1
        else:
            s.add(cards[i])
    
    return cnt
# Generator time: 11.1574 seconds