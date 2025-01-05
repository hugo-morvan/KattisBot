def nim_game(n, piles):
    # Calculate the XOR of the number of stones in each pile
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    
    # If the XOR sum is zero, the second player (Bob) wins
    # If the XOR sum is non-zero, the first player (Alice) wins
    return 1 if xor_sum != 0 else 0

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        piles = list(map(int, input().split()))
        
        result = nim_game(n, piles)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 15.6953 seconds