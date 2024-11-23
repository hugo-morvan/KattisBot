def max_web_servers(n, servers):
    # Initialize the count of working servers
    working_servers = 0
    
    # Iterate over each web server
    for i in range(n):
        # Check if the current web server is already working
        if servers[i][0] == 'J' and servers[i][1] == 'J' and servers[i][2] == 'J':
            working_servers += 1
            continue
        
        # Try to swap parts to make the current web server work
        for j in range(n):
            if i != j:
                # Check if the other web server has at least one missing component
                if (servers[j][0] == 'N' and servers[i][0] == 'J') or \
                   (servers[j][1] == 'N' and servers[i][1] == 'J') or \
                   (servers[j][2] == 'N' and servers[i][2] == 'J'):
                    # Swap components
                    servers[i], servers[j] = servers[j], servers[i]
                    working_servers += 1
                    break
    
    return working_servers

# Read input
n = int(input())
servers = [input().strip() for _ in range(n)]

# Calculate and print the result
result = max_web_servers(n, servers)
print(result)