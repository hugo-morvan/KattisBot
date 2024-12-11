# Read input values
R, C, Z_R, Z_C = map(int, input().split())
article = [input() for _ in range(R)]

# Initialize the result matrix
result = [['.' for _ in range(C * Z_C)] for _ in range(R * Z_R)]

# Enlarge the article
for r in range(R):
    for c in range(C):
        char = article[r][c]
        for i in range(Z_R):
            for j in range(Z_C):
                result[r * Z_R + i][c * Z_C + j] = char

# Print the result
for row in result:
    print(''.join(row))