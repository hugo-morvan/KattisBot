import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    W = int(data[1])
    H = int(data[2])
    
    matches = [int(data[i]) for i in range(3, N + 3)]
    
    for match_length in matches:
        if match_length <= W or match_length <= H:
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()