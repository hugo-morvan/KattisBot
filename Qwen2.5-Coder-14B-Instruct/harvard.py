def parse_program(program):
    stack = []
    for token in program:
        if token.startswith('R'):
            count = int(token[1:])
            stack.append(('R', count))
        elif token == 'E':
            subprogram = []
            while True:
                last = stack.pop()
                if last == ('R', 0):
                    break
                subprogram.append(last)
            stack.append(subprogram[::-1])
        else:
            stack.append(token)
    return stack

def flatten_program(program):
    flattened = []
    for item in program:
        if isinstance(item, list):
            flattened.extend(flatten_program(item))
        else:
            flattened.append(item)
    return flattened

def calculate_min_instructions(b, s, program):
    from collections import defaultdict
    
    # Flatten the program
    flat_program = flatten_program(parse_program(program.split()))
    
    # Count occurrences of each variable reference
    var_count = defaultdict(int)
    for token in flat_program:
        if token.startswith('V'):
            var_index = int(token[1:])
            var_count[var_index] += 1
    
    # Calculate minimum instructions
    instructions = 0
    bsr_changes = 0
    current_bank = None
    
    for var_index in sorted(var_count.keys()):
        bank = (var_index - 1) // s
        if bank != current_bank:
            bsr_changes += 1
            current_bank = bank
        instructions += var_count[var_index]
    
    return instructions + bsr_changes

def main():
    import sys
    
    # Read input
    lines = sys.stdin.read().splitlines()
    b, s = map(int, lines[0].split())
    program = lines[1]
    
    # Calculate and print the minimum number of instructions
    result = calculate_min_instructions(b, s, program)
    print(result)

if __name__ == "__main__":
    main()
# Generator time: 52.5387 seconds