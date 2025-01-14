 n0 = 1.0
n1 = 1000000.0
t0 = 'A' + "'"
t1 = t0 * 2.0
answer = len(t1) - (len('B') % 3)
print(answer)
# Generator time: 3.7480 seconds