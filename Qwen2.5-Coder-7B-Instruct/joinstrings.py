# Fast input and output using sys module
import sys
input = sys.stdin.read
output = sys.stdout.write

# Read input data
data = input().split()

# Number of strings
N = int(data[0])

# Initialize list to store strings
strings = data[1:N+1]

# Index to keep track of the current position in the data list
index = N + 1

# Process each operation
for _ in range(N - 1):
    a = int(data[index]) - 1  # Convert to 0-based index
    b = int(data[index + 1]) - 1  # Convert to 0-based index
    index += 2
    
    # Concatenate strings and make the second string empty
    strings[a] += strings[b]
    strings[b] = ""

# The last remaining string is at index N-1 in the list of strings
result = "".join(strings)
print(result)
# Generator time: 7.7344 seconds