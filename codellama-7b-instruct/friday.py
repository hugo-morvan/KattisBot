n_cases=int(input())
for t in range(n_cases):
    D,M=map(int,input().split())
    d=[int(x) for x in input().split()]
    if M == 12:
        print(D)
    else:
        count = 0
        for i in range(len(d)):
            if i < M - 1 and (d[i] + count) % 7 == 3:
                count += d[i]
            elif i == M - 1 and (d[i] + count) % 7 == 2:
                count += d[i]
        print(D - count)
# Generator time: 5.7011 seconds