import re
r = re.compile(r'(\d+)') # r is a regular expression object to find numbers in the string
def evaluate(s):
    v = 0
    for m in r.finditer(s):
        v += int(m.group())
    return v
    
for line in sys.stdin:
    R, C = [int(x) for x in line.split()] # R is the number of rows and C is the number of columns
    screen = [input() for _ in range(R)]
    V = 0
    for i in range(R):
        if '+' in screen[i]:
            v1, v2 = screen[i].split('+')
            v3 = evaluate(v1) + evaluate(v2)
            V += v3
        elif '-' in screen[i]:
            v1, v2 = screen[i].split('-')
            v3 = evaluate(v1) - evaluate(v2)
            V += v3
        else:
            V += evaluate(screen[i])
    print(V)
# Generator time: 10.2871 seconds