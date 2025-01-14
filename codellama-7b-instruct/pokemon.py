c = int(input())
r = int(input())
grid = input().split()

moves_needed = {}

for i in range(len(grid)):
    moves_needed[i] = -1

def move(start, end):
    if grid[end] == '.':
        return 0
    
    elif grid[end] == '#':
        return -1
    
    elif grid[end] == '_':
        return 1 + move(start, end-c)
    
    else:
        return -1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'M':
            moves_needed[i*c+j] = move(i*c+j, (i-1)*c+(j-1)) + 1
# Generator time: 6.8677 seconds