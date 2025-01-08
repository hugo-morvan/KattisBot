import sys

def find_first_breach_wave(N, R):
    # Find the minimum number of peashooters across all rows
    min_peashooters = min(R)
    
    # The first wave that will breach the defense is when the number of bad guys
    # exceeds the minimum number of peashooters in any row
    return min_peashooters + 1

if __name__ == "__main__":
    N = int(input().strip())
    R = list(map(int, input().strip().split()))
    
    result = find_first_breach_wave(N, R)
    print(result)
# Generator time: 19.0529 seconds