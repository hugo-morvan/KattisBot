 n=int(input())
l=[int(x)for x in input().split()]
t=-(-max(l)//sum([-(-i//2) for i in range(1,n+1)]))
# Generator time: 3.5694 seconds