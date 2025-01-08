def calculate_unread_messages(n, m, messages):
    last_message_time = [0] * n
    total_unread = 0
    unread_count = [0] * m

    for i in range(m):
        sender = messages[i] - 1
        if last_message_time[sender] == 0:
            total_unread += m - i
        else:
            total_unread -= last_message_time[sender]
            total_unread += m - (i + 1)
        
        unread_count[i] = total_unread
        last_message_time[sender] = m - (i + 1)

    return unread_count

# Read input
n, m = map(int, input().split())
messages = [int(input()) for _ in range(m)]

# Calculate and print the result
unread_messages = calculate_unread_messages(n, m, messages)
for count in unread_messages:
    print(count)
# Generator time: 26.1320 seconds