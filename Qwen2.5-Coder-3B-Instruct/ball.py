def find_prankster_pair(n):
    # Create a dictionary to count occurrences of each pair
    pair_count = {}
    
    # Read the input pairs
    for _ in range(n // 2 + 1):
        a, b = map(int, input().split())
        # Add the pair to the dictionary
        pair_count[(min(a, b), max(a, b))] = pair_count.get((min(a, b), max(a, b)), 0) + 1
    
    # Find the pair with an odd count
    for pair, count in pair_count.items():
        if count % 2 == 1:
            return f"{pair[0]} {pair[1]}"
    
    # In case no pair is found (should not happen due to problem constraints)
    return ""

# Read the input value of n
n = int(input())

# Find and print the prankster's pair
print(find_prankster_pair(n))
# Generator time: 19.4043 seconds