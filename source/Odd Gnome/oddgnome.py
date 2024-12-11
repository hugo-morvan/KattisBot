import sys

def find_king_position(n):
    for _ in range(n):
        g = int(input())
        gnomes = list(map(int, input().split()))
        
        for i in range(g):
            if gnomes[i] != gnomes[i - 1] + 1:
                print(i + 1)
                break

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    find_king_position(n)