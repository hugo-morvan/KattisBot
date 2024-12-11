def check_order(names):
    increasing = all(names[i] <= names[i + 1] for i in range(len(names) - 1))
    decreasing = all(names[i] >= names[i + 1] for i in range(len(names) - 1))
    
    if increasing:
        return "INCREASING"
    elif decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

# Read input
N = int(input())
names = [input() for _ in range(N)]

# Determine the order
result = check_order(names)

# Output the result
print(result)