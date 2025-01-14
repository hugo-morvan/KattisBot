import math
N=int(input())
K=0
for i in range(N//2):
    K*=10
    K+=int(input()[:-1])
M=math.ceil(math.sqrt(K))
print((M*(M+1)*(M+2)//6)%(10**9+7))
# Generator time: 4.5156 seconds