c,t = map(int,input().split())
chambers = [i for i in range(1,c+1)]

for _ in range(t):
    a,b = map(int,input().split())
    chambers[a-1],chambers[b-1] = chambers[b-1],chambers[a-1]

visited = [False for i in chambers]
p = 0
for i in range(len(chambers)):
    if not visited[i]:
        while not visited[i]:
            p += 1
            visited[i] = True
            i = chambers[i-1]
            
visited = [False for i in chambers]
s = c - p
for i in range(len(chambers)):
    if not visited[i]:
        while not visited[i]:
            s += 1
            visited[i] = True
            i = chambers[i-1]
            
print(p,s)
print(*chambers[:p],sep=' ')
for i in range(len(chambers)):
    if not visited[i]:
        print(chambers[i])
# Generator time: 8.6115 seconds