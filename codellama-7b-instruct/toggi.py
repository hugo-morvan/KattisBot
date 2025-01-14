import math
def solve(C):
    return int(math.ceil(min(C * 10**6 / math.log(10), 10**9)))
# Generator time: 4.5678 seconds