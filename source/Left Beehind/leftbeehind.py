while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    
    if x > y:
        print("Left beehind.")
    elif x < y:
        print("To the convention.")
    elif x == y:
        print("Undecided.")
    else:
        print("Never speak again.")