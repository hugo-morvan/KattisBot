def find_matching_indices():
    # Read input
    n, m = map(int, input().split())
    
    map1 = [input().strip() for _ in range(n)]
    map2 = [input().strip() for _ in range(m)]
    
    # Initialize counters
    count = 0
    
    # Iterate over possible starting positions of the second map on the first map
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if map1[i + j] != '?' and map2[j] != '?' and map1[i + j] != map2[j]:
                match = False
                break
        if match:
            count += 1
    
    # Output the result
    print(count)

# Call the function to execute the code
find_matching_indices()
# Generator time: 7.3141 seconds