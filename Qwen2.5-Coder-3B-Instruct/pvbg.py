def main():
    # Read the number of rows
    N = int(input())
    
    # Read the number of peashooters for each row
    R = list(map(int, input().split()))
    
    # Initialize the wave number
    t = 1
    
    # Iterate over each wave
    while True:
        # Check if any row has more bad guys than peashooters
        if any(bad_guys > peashooters for bad_guys, peashooters in zip(range(1, t + 1), R)):
            break
        t += 1
    
    # Print the first wave where the bad guys can reach Mikael
    print(t)

if __name__ == "__main__":
    main()
# Generator time: 22.2025 seconds