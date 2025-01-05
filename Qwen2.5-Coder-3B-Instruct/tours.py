def find_valid_bus_companies(n, m, roads):
    # Initialize a set to store valid numbers of bus companies
    valid_k = set()
    
    # Iterate over possible numbers of bus companies from 1 to m
    for k in range(1, m + 1):
        # Check if m is divisible by k
        if m % k == 0:
            valid_k.add(k)
    
    # Convert the set to a sorted list and print
    sorted_valid_k = sorted(valid_k)
    print(" ".join(map(str, sorted_valid_k)))

# Read input
n = int(input())
m = int(input())
roads = []
for _ in range(m):
    a, b = map(int, input().split())
    roads.append((a - 1, b - 1))  # Adjusting indices to be 0-based

# Find and print valid bus companies
find_valid_bus_companies(n, m, roads)
# Generator time: 21.1790 seconds