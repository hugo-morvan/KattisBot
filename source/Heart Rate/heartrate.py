import sys

def calculate_bpm(b, p):
    # Calculate the BPM using the formula 60b / p
    bpm = 60 * b / p
    return bpm

def main():
    N = int(input())
    
    for _ in range(N):
        b, p = map(float, input().split())
        
        # Calculate the actual BPM (ABPM)
        abpm = 60 / p
        
        # Calculate the minimum possible ABPM
        min_abpm = 60 / (p + 0.0001)
        
        # Calculate the maximum possible ABPM
        max_abpm = 60 / (p - 0.0001)
        
        # Print the results
        print(f"{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}")

if __name__ == "__main__":
    main()