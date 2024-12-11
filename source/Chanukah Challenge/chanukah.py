def main():
    # Read the number of data sets
    P = int(input())
    
    for _ in range(P):
        # Read the data set number and the number of days
        K, N = map(int, input().split())
        
        # Calculate the total number of candles needed
        total_candles = (N * (N + 1)) // 2 + N
        
        # Print the result
        print(f"{K} {total_candles}")

if __name__ == "__main__":
    main()