def count_unread_messages(n, m):
    # Initialize the unread message count for each member
    unread_counts = [0] * (n + 1)
    
    # Process each message
    for i in range(m):
        sender = int(input())
        unread_counts[sender] += 1
    
    # Compute the total unread messages after each message is sent
    total_unread = 0
    for i in range(1, n + 1):
        total_unread += unread_counts[i]
        print(total_unread)

# Read input
n, m = map(int, input().split())
count_unread_messages(n, m)
# Generator time: 6.1225 seconds