import sys
from math import sqrt

def parse_integer(matrix, start, end):
    return int(''.join(matrix[start][i] for i in range(start[1], end[1])))

def parse_term(matrix, start, end):
    if ' ' in matrix[start]:
        space_index = matrix[start].index(' ')
        left_value = parse_integer(matrix, (start[0], start[1]), (start[0], space_index))
        right_value = parse_term(matrix, (start[0], space_index + 2), end)
        return left_value * right_value
    else:
        return parse_integer(matrix, start, end)

def parse_simple(matrix, start, end):
    if '+' in matrix[start]:
        plus_index = matrix[start].index('+')
        left_value = parse_term(matrix, (start[0], start[1]), (start[0], plus_index))
        right_value = parse_simple(matrix, (start[0], plus_index + 2), end)
        return left_value + right_value
    elif '-' in matrix[start]:
        minus_index = matrix[start].index('-')
        left_value = parse_term(matrix, (start[0], start[1]), (start[0], minus_index))
        right_value = parse_simple(matrix, (start[0], minus_index + 2), end)
        return left_value - right_value
    else:
        return parse_term(matrix, start, end)

def parse_complex(matrix, start, end):
    if matrix[start][0] == '/':
        bar_length = 0
        while matrix[start][bar_length] == '_':
            bar_length += 1
        sqrt_value = parse_simple(matrix, (start[0] + 2, start[1]), (end[0], start[1] + bar_length))
        return int(sqrt(sqrt_value))
    elif '=======' in ''.join(matrix[start]):
        fraction_bar_index = next(i for i, row in enumerate(matrix) if '=======' in row)
        numerator_start = (start[0], 0)
        numerator_end = (fraction_bar_index - 1, len(matrix[fraction_bar_index]) - 1)
        denominator_start = (fraction_bar_index + 2, 0)
        denominator_end = (end[0], len(matrix[end[0]]) - 1)
        numerator_value = parse_simple(matrix, numerator_start, numerator_end)
        denominator_value = parse_simple(matrix, denominator_start, denominator_end)
        return numerator_value // denominator_value
    else:
        return parse_simple(matrix, start, end)

def parse_formula(matrix, start, end):
    if '+' in matrix[start]:
        plus_index = next(i for i, row in enumerate(matrix) if '+' in row)
        left_value = parse_complex(matrix, (start[0], start[1]), (plus_index - 1, len(matrix[plus_index - 1]) - 1))
        right_value = parse_formula(matrix, (plus_index + 2, 0), end)
        return left_value + right_value
    elif '-' in matrix[start]:
        minus_index = next(i for i, row in enumerate(matrix) if '-' in row)
        left_value = parse_complex(matrix, (start[0], start[1]), (minus_index - 1, len(matrix[minus_index - 1]) - 1))
        right_value = parse_formula(matrix, (minus_index + 2, 0), end)
        return left_value - right_value
    else:
        return parse_complex(matrix, start, end)

def evaluate_formula(R, C, matrix):
    return parse_formula(matrix, (0, 0), (R - 1, C - 1))

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    while index < len(data):
        R, C = map(int, data[index].split())
        matrix = []
        for _ in range(R):
            index += 1
            matrix.append(data[index])
        index += 1
        
        result = evaluate_formula(R, C, matrix)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 113.4617 seconds