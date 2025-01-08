def min_instructions(b, s, program):
    from collections import defaultdict

    # Parse the program
    tokens = program.split()
    i = 0
    parsed_program = []
    while i < len(tokens):
        token = tokens[i]
        if token == 'R':
            n = int(tokens[i + 1])
            subprogram_start = i + 2
            while tokens[subprogram_start] != 'E':
                subprogram_start += 1
            subprogram = ' '.join(tokens[i + 2:subprogram_start])
            parsed_program.append((n, subprogram))
            i = subprogram_start + 1
        else:
            parsed_program.append(token)
            i += 1

    # Helper function to calculate the minimum instructions for a subprogram
    def min_instructions_subprogram(subprogram):
        stack = []
        bsr_map = defaultdict(int)
        last_bank = -1

        for token in subprogram.split():
            if token.startswith('V'):
                var_index = int(token[1:])
                bank_index = (var_index - 1) // s
                if bank_index != last_bank:
                    last_bank = bank_index
                    bsr_map[bank_index] += 1

            elif token.startswith('R'):
                n, subprogram_sub = min_instructions_subprogram(subprogram_sub)
                for _ in range(n):
                    stack.extend(min_instructions_subprogram(subprogram_sub))

        return sum(bsr_map.values()), len(stack)

    # Calculate the minimum instructions for the entire program
    total_bsr_settings, total_instructions = min_instructions_subprogram(' '.join(map(str, parsed_program)))

    return total_bsr_settings + total_instructions

# Read input
b, s = map(int, input().split())
program = input()

# Output the result
print(min_instructions(b, s, program))
# Generator time: 11.9642 seconds