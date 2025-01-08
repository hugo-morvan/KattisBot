def can_win(n, piles):
    total_piles = n
    total_stones = sum(piles)
    
    # If there are an even number of piles and each pile has more than one stone,
    # then Bob can always mirror Alice's moves and win.
    if total_piles % 2 == 0 and all(s > 1 for s in piles):
        return False
    
    # Otherwise, Alice can always make a move that leaves an odd number of piles
    # with at least one stone each, ensuring she wins.
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        piles = list(map(int, data[index:index + n]))
        index += n
        
        if can_win(n, piles):
            results.append(1)
        else:
            results.append(0)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 33.1656 seconds