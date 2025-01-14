for t in range(int(input())):
    x_size = int(input())
    y_size = int(input())
    start_pos = list(map(int, input().split(" ")))
    beepers = int(input())
    pos_list = []
    
    for i in range(beepers):
        temp = list(map(int, input().split(" ")))
        pos_list.append(temp)
    
    distance = 0
    for j in range(len(pos_list)):
        if start_pos[1] > pos_list[j][1]: # up
            distance += start_pos[1] - pos_list[j][1] + 1
        elif start_pos[1] == pos_list[j][1]:
            if start_pos[0] < pos_list[j][0]: # left
                distance += abs(start_pos[0] - pos_list[j][0])
            else:
                distance += x_size - abs(start_pos[0] - pos_list[j][0]) + 1
        elif start_pos[1] < pos_list[j][1]: # down
            distance += pos_list[j][1] - start_pos[1] + 1
        
    print(distance)
# Generator time: 8.7506 seconds