def evaluate_formula(formula):
    def parse_term():
        if formula[idx].isdigit():
            num = 0
            while idx < len(formula) and formula[idx].isdigit():
                num = num * 10 + int(formula[idx])
                idx += 1
            return num
        elif formula[idx] == '(':
            idx += 1
            result = parse_formula()
            assert formula[idx] == ')'
            idx += 1
            return result
        else:
            raise ValueError("Unexpected character in term")

    def parse_simple():
        if formula[idx] == '/':
            idx += 1
            length = 0
            while idx < len(formula) and formula[idx] == '_':
                length += 1
                idx += 1
            return length

        elif formula[idx] == '=':
            numerator = parse_simple()
            if idx >= len(formula) or formula[idx] != '=':
                raise ValueError("Invalid fraction format")
            idx += 1
            denominator = parse_simple()
            return numerator // denominator

        else:
            return parse_term()

    def parse_complex():
        result = parse_simple()
        while idx < len(formula):
            if formula[idx] == '+':
                idx += 2
                result += parse_simple()
            elif formula[idx] == '-':
                idx += 2
                result -= parse_simple()
            else:
                break
        return result

    def parse_sqrt():
        nonlocal idx
        if idx + len("sqrt") <= len(formula) and formula[idx:idx+len("sqrt")] == "sqrt":
            idx += 4
            length = parse_simple()
            if length != 0:
                idx += 2 * length  # Skip the bar and underbar
            return length
        else:
            raise ValueError("Invalid sqrt format")

    def parse_fraction():
        nonlocal idx
        if formula[idx] == '=' and idx + 1 < len(formula) and formula[idx+1] == '=':
            numerator = parse_simple()
            if idx + 2 >= len(formula) or formula[idx+2] != '=':
                raise ValueError("Invalid fraction format")
            idx += 3
            denominator = parse_simple()
            return numerator // denominator
        else:
            raise ValueError("Invalid fraction format")

    def parse_formula():
        result = parse_complex()
        while idx < len(formula):
            if formula[idx] == '+':
                idx += 2
                result += parse_complex()
            elif formula[idx] == '-':
                idx += 2
                result -= parse_complex()
            else:
                break
        return result

    global idx
    idx = 0
    return parse_formula()

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    for i in range(1, len(data), 2):
        R, C = map(int, data[i].split())
        formula = data[i+1]
        result = evaluate_formula(formula)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 19.9195 seconds