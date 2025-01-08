n, m = map(int, input().split())
last_message_time = [-1] * (n + 1)
unread_messages = [0] * n

for _ in range(m):
    sender = int(input())
    last_message_time[sender] = _
    unread_messages[sender - 1] += 1
    for i in range(1, n + 1):
        if last_message_time[i] < _:  # If the person received a message before this one
            unread_messages[i - 1] += 1
    print(sum(unread_messages))
# Generator time: 5.8176 seconds