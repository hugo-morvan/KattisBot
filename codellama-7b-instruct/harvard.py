import sys
def parse(program):
    stack = []
    result = ""
    for i in range(len(program)):
        if program[i] == 'E':
            if len(stack) < 1:
                return "Bad program"
            op, n = stack.pop()
            if op == 'R':
                result += (str(n) + ' ')
            else:
                result += ('V' + str(i // s + 1) + ' ')
        else:
            stack.append((program[i], int(program[i+1])))
    return "Bad program" if len(stack) > 0 else result[:-1]
def run(m, x):
    b = m // x
    s = x
    var_index = 0
    mem = [[] for _ in range(b)]
    for i in range(len(x)):
        if x[i] == 'V':
            mem[var_index // s].append(i)
            var_index += 1
        elif x[i] == 'R':
            n = int(x[i+1])
            for j in range(n):
                if len(mem[var_index % b]) == 0:
                    return sys.maxsize
                mem[var_index % b].pop()
            var_index += s * n
    return var_index // s + 1
def solve(m, x):
    parsed = parse(x)
    if parsed == "Bad program":
        return parsed
    else:
        t = []
        for i in range(len(parsed)):
            if parsed[i] == 'V':
                t.append((run(m, x[:i]), run(m, x[i+1:])))
            elif parsed[i] == 'R':
                t.append((run(m, x[:i]) + int(parsed[i+1]), run(m, x[i+2:])))
        return min([j for i in t for j in range(i[0], i[1] + 1)])
# Generator time: 14.3315 seconds