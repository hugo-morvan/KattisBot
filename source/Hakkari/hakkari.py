import sys

def main():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    
    mines = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                mines.append((i + 1, j + 1))
    
    print(len(mines))
    for r, c in mines:
        print(r, c)

if __name__ == "__main__":
    main()