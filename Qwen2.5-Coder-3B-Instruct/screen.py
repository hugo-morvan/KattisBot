import sys
from math import sqrt

def parse_formula(formula):
    lines = formula.split('\n')
    R, C = len(lines), len(lines[0])
    
    def parse_term(line, start):
        end = start
        while end < C and line[end].isdigit():
            end += 1
        term = int(line[start:end])
        if end < C and line[end] == '*':
            end += 1
            term *= parse_term(line, end)
        return term
    
    def parse_simple(line, start):
        end = start
        while end < C and line[end].isdigit():
            end += 1
        simple = parse_term(line, start)
        if end < C:
            if line[end] == '+':
                end += 1
                simple += parse_simple(line, end)
            elif line[end] == '-':
                end += 1
                simple -= parse_simple(line, end)
        return simple
    
    def parse_sqrt(line, start):
        end = start
        while end < C and line[end] == '_':
            end += 1
        length = end - start
        simple = parse_simple(line, start + length)
        return int(sqrt(simple))
    
    def parse_fraction(line, start):
        end = start
        while end < C and line[end] == '=':
            end += 1
        top_length = end - start
        top = parse_simple(line, start)
        bottom_length = C - end
        bottom = parse_simple(line, end)
        return top // bottom
    
    def parse_complex(line, start):
        end = start
        if line[end] == '/':
            end += 1
            return parse_sqrt(line, end)
        else:
            return parse_simple(line, end)
    
    def parse_formula(line, start):
        end = start
        while end < C and line[end].isdigit():
            end += 1
        formula = parse_complex(line, start)
        if end < C and line[end] in ['+', '-', '*']:
            end += 1
            formula += parse_formula(line, end)
        elif end < C and line[end] == '-':
            end += 1
            formula -= parse_formula(line, end)
        return formula
    
    return parse_formula(lines[0], 0)

def main():
    for line in sys.stdin:
        R, C = map(int, line.strip().split())
        formula = ''
        for _ in range(R):
            formula += next(sys.stdin)
        result = parse_formula(formula)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 25.8519 seconds