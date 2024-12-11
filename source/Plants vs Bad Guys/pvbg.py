def main():
    N = int(input())
    R = list(map(int, input().split()))
    
    max_peashooters = max(R)
    min_waves = 1
    
    while True:
        for i in range(N):
            if R[i] < min_waves:
                return min_waves
        min_waves += 1

if __name__ == "__main__":
    main()