 n0 = 3.0
n1 = 60.0
n2 = 1.0
n3 = 10.0
n4 = 20.0
t0 = -1000.0
t1 = t0 + 1000.0
fst = [None, n0]
snd = [[], fst[i%2:][::-1]]
def solve(x=n3): # x is d in the problem statement
# Generator time: 4.9137 seconds