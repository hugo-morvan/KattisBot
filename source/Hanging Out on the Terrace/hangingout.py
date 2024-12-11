# Read input
L, x = map(int, input().split())
events = [input().split() for _ in range(x)]

# Initialize variables
current_people = 0
denied_count = 0

# Process each event
for event in events:
    action = event[0]
    p = int(event[1])

    if action == "enter":
        # Check if adding the new group would exceed the limit
        if current_people + p > L:
            denied_count += 1
        else:
            current_people += p
    elif action == "leave":
        current_people -= p

# Output the result
print(denied_count)