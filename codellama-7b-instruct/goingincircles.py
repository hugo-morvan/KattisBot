
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    
    s = int(input())
    
    for i in range (3*n+500):
        print(s)
        
        if s == 1:
            s = 0
        else:
            s = 1
            
    print("!", n)
# Generator time: 4.5176 seconds