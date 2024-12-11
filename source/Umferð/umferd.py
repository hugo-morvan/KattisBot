def calculate_empty_cells():
    m = int(input())
    n = int(input())
    total_cells = m * n
    empty_cells = 0

    for _ in range(n):
        lane = input()
        for cell in lane:
            if cell == '.':
                empty_cells += 1

    empty_proportion = empty_cells / total_cells
    print(empty_proportion)

calculate_empty_cells()