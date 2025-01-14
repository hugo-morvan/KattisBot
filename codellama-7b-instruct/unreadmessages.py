n, m = map(int, input().split())
messages = []
for _ in range(m):
    messages.append(set())
unread_messages = [0] * (n+1)
for i in range(m):
    s = int(input())
    unread_messages[s] += 1
    messages[i-1].add(s)
    for j in range(i, m):
        if len(messages[j]) == 0: continue
        if messages[j].issubset(messages[i-1]): unread_messages[s] -= len(messages[j])
    print(sum(unread_messages))
# Generator time: 5.6077 seconds