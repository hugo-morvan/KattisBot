def anti11(s):
    return s.count('1') == s.count('0')
    

for case in range(int(input())):
    n = int(input())
    
    count = 0
    for i in range(2**n):
        binary_string = bin(i)[2:]
        
        if anti11(binary_string):
            count += 1
            
    print((count % (10**9 + 7)))
# Generator time: 4.8777 seconds