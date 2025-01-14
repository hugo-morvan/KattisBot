import sys
import math
def get_row(badguys):
    rows = []
    for i in range(len(badguys)):
        if badguys[i] not in rows:
            rows.append(badguys[i])
        else:
            return -1
    return len(rows)
def peashooter_solution():
    input_reader = sys.stdin
    N = int(input_reader.readline().strip())
    R_list = [int(x) for x in input_reader.readline().split()]
    badguys = list(map(int, input_reader.readline().split()))
    row_count = get_row(badguys)
    
    if N == 1:
        if R_list[0] >= len(badguys):
            print("1")
        else:
            print(-1)
    elif row_count == -1:
        print(-1)
    else:
        R = max(R_list)
        if R >= row_count * badguys[0]:
            print("1")
        else:
            print(-1)

peashooter_solution()
# Generator time: 13.1511 seconds