 ```python3
from itertools import combinations
import math
def shortest_path(start,beep):
    #print("Start", start) 
    distance = abs(int(start[0]) - int(beep[0])) + abs(int(start[1])-int(beep[1]));  
    
    return (distance);     
def shortest_path2():
    for _ in range(scenarios): # number of scenarios given as first line input 
        world = list(map(int,input().split()))[:-3]# x and y size  
         start=list(map(float,(input()).rstrip().split(" ")))[0:2];     #[x1 ,y1 ] # starting position of Karel.    beepers_no = list(map(int, input().split()))  [beeper no]      beepersposition={};
        for i in range (len(beepers_no)):   # loop to get all the positions and store as key value pairs {position:value}         xy=list((input()).rstrip().split(" "));    
            if len(xy) == 2:# condition check whether position of beeper is in x,y format         
                beepers_no[i]=float(beepers_no[i])    # converting into integer as it was string earlier           xy.append((int)(beepers_no[i]))         key=(xy)      value=shortest_path2([start],key);        beepersposition[(list)((str)(key))] =value;      
          return (len(combinations(values(), 1))) # printing the shortest path to get all beepers and back
# Generator time: 10.7265 seconds