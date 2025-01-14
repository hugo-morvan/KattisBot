x=input()
y=map(int,raw_input().split())
ships=[0]*len(y)
bombs=[]
for i in range(len(y)):
    ships[i]=[float(y[3*i]),float(y[3*i+1]),float(y[3*i+2])]
    bombs.append([0]*3)
for j in range(len(ships)):
    for k in range(len(bombs)):
        if(abs(ships[j][0]-bombs[k][0])<=bombs[k][2] and abs(ships[j][1]-bombs[k][1])<=bombs[k][2] and abs(ships[j][2]-bombs[k][2])<=bombs[k][2]):
            print("0")
            exit()
print("1")
# Generator time: 7.4460 seconds