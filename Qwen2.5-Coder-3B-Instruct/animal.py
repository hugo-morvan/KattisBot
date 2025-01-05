def parse_tree(s):
    stack = []
    current_group = []
    for char in s:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ',':
            stack[-1].append(current_group)
            current_group = []
        elif char == ')':
            if stack:
                current_group = stack.pop()
            else:
                break
        else:
            current_group.append(int(char))
    return current_group

def find_common_groups(alice_tree, bob_tree):
    alice_groups = set(parse_tree(alice_tree))
    bob_groups = set(parse_tree(bob_tree))
    common_groups = alice_groups.intersection(bob_groups)
    return len(common_groups)

# Read input
N = int(input())
alice_tree = input()
bob_tree = input()

# Find and print the number of common groups
common_count = find_common_groups(alice_tree, bob_tree)
print(common_count)
# Generator time: 22.3570 seconds