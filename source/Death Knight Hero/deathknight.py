n = int(input())
wins = 0

for _ in range(n):
    abilities = input().strip()
    win = True
    
    for i in range(len(abilities) - 1):
        if abilities[i] == 'C' and abilities[i + 1] == 'D':
            win = False
            break
    
    if win:
        wins += 1

print(wins)