def count_towers():
    N = int(input())
    bricks = list(map(int, input().split()))
    
    current_tower_width = 0
    tower_count = 0
    
    for brick in bricks:
        if brick > current_tower_width:
            current_tower_width = brick
            tower_count += 1
    
    print(tower_count)

count_towers()