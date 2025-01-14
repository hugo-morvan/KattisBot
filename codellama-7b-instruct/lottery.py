import math
def solve(m, n, t, p):
    if m < p: return 0

    num = math.factorial(m) * math.factorial(n-1) * math.factorial(t) * math.factorial(m-n*t)
    den = math.factorial(m) * math.factorial(n-1) * math.factorial(p) * math.factorial(m-p*t)
    return num / den
# Generator time: 4.8961 seconds