# Read the number of meat types
n = int(input())

# Read the meat types
meat_types = [input() for _ in range(n)]

# Check if Níels gets both types
if 'nautakjot' in meat_types and 'kjuklingur' in meat_types:
    print("blandad best")
elif 'nautakjot' in meat_types:
    print("nautakjot")
else:
    print("kjuklingur")