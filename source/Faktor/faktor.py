import math

# Read input values
A, I = map(int, input().split())

# Calculate the required number of citations
required_citations = I * A

# Calculate the minimum number of scientists needed to achieve the required citations
min_bribes = math.ceil(required_citations / A)

# Output the result
print(min_bribes)