while True:
    num, denom = map(int, input().split())
    if num == 0 and denom == 0:
        break
    
    whole = num // denom
    remainder = num % denom
    
    if remainder == 0:
        print(f"{whole} {remainder}/{denom}")
    else:
        print(f"{whole} {remainder}/{denom}")