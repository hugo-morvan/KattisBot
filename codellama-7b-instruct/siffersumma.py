n=int(input())
digitsum=sum(map(int,str(n)))
nextn=(10**(len(str(n))))+n
while digitsum==sum(map(int,str(nextn))):
    nextn+=1
print(nextn)
# Generator time: 7.5102 seconds