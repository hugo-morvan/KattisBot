H,N,M = map(int,input().split())
C = []
F = []
for i in range(N):
    C.append([])
    F.append([])
    for j in range(M):
        C[i].append(int(input()))
        F[i].append(int(input()))
t = 0
while t < H:
    if t == 50:
        break
    for i in range(N):
        for j in range(M):
            if t + 10 <= C[i][j] and F[i][j] - 50 <= F[i-1][j] and F[i][j] - 50 <= F[i+1][j] and F[i][j] - 50 <= F[i][j-1] and F[i][j] - 50 <= F[i][j+1]:
                t += 1
                
for i in range(N):
    for j in range(M):
        if C[i][j] - 50 < F[i][j] and F[i][j] < C[i][j] + 50:
            print('Case #1:', t)
            break
        elif j == M-1:
            print('Case #1:', t+3)
            break
# Generator time: 18.5805 seconds