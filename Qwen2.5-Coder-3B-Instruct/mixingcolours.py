def calculate_most_likely_colour(rules, sequence):
    # Convert rules into a dictionary for quick lookup
    rule_dict = {}
    for rule in rules:
        a, b, c = rule.split()
        rule_dict[(a, b)] = c
    
    # Initialize the stack with the sequence
    stack = sequence[:]
    
    while len(stack) > 1:
        # Try to find a valid combination
        for i in range(len(stack) - 1):
            a, b = stack[i], stack[i + 1]
            if (a, b) in rule_dict:
                # Combine them and replace the pair
                stack[i:i+2] = [rule_dict[(a, b)]]
                break
        else:
            # No valid combination found, game over
            return "GAMEOVER"
    
    # The result is the last remaining token
    return stack[0]

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse rules
R = int(data[0])
rules = []
for _ in range(R):
    rules.append(data[1 + _ * 3: 1 + (_ + 1) * 3])

# Parse test cases
T = int(data[1 + R * 3])
for _ in range(T):
    C = int(data[1 + R * 3 + 1 + _ * 2])
    sequence = []
    while True:
        token = data[1 + R * 3 + 2 + _ * 2 + C]
        if token == "END":
            break
        cer, color = map(float, token.split())
        sequence.append((color, cer))
    
    # Calculate the most likely colour
    result = calculate_most_likely_colour(rules, sequence)
    print(result)
# Generator time: 18.1596 seconds