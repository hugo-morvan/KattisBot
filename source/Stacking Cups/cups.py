def sort_cups(messages):
    cups = []
    
    for message in messages:
        parts = message.split()
        color = parts[0]
        value = int(parts[1])
        
        # Adjust the value based on the type of message
        if len(parts) == 3:
            value *= 2
        
        cups.append((value, color))
    
    # Sort cups by radius
    cups.sort()
    
    # Extract and print the sorted colors
    for _, color in cups:
        print(color)

# Read input
N = int(input())
messages = [input() for _ in range(N)]

# Process and output the sorted cups
sort_cups(messages)