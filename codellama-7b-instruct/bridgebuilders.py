def find_solution(matrix):
    forest_count = 0
    island_count = 0

    for row in matrix:
        for col in row:
            if col == "T":
                forest_count += 1
            elif col != ".":
                island_count += 1

    solution = 0

    for i in range(forest_count):
        for j in range(island_count):
            if matrix[i][j] == "T" and matrix[i][j + 1] != ".":
                solution += len(matrix) - i
            elif matrix[i][j] == "T" and matrix[i + 1][j] != ".":
                solution += len(matrix) - i

    return solution
# Generator time: 6.4258 seconds