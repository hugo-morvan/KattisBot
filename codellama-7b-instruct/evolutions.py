import math

def count_CPsequence(S):
    i = 1
    while True:
        j = math.ceil(math.pow(2, i)) - 1
        if j * (j + 1) // 2 == S:
            return i
        elif j * (j + 1) // 2 > S:
            return i - 1
        else:
            i = i + 1
# Generator time: 4.8193 seconds