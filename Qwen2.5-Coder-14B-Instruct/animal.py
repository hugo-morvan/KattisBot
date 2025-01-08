def parse_tree(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append([])
        elif char.isdigit():
            stack[-1].append(int(char))
        elif char == ')':
            subtree = stack.pop()
            if len(stack) > 0:
                stack[-1].append(subtree)
            else:
                return subtree

def get_groups(tree):
    groups = set()
    def dfs(node, current_group):
        if isinstance(node, int):
            current_group.add(node)
            groups.add(frozenset(current_group))
        elif isinstance(node, list):
            for child in node:
                dfs(child, current_group.copy())
    dfs(tree, set())
    return groups

def count_common_groups(alice_tree, bob_tree):
    alice_groups = get_groups(alice_tree)
    bob_groups = get_groups(bob_tree)
    common_groups = alice_groups.intersection(bob_groups)
    return len(common_groups)

N = int(input().strip())
alice_tree_str = input().strip()
bob_tree_str = input().strip()

alice_tree = parse_tree(alice_tree_str)
bob_tree = parse_tree(bob_tree_str)

result = count_common_groups(alice_tree, bob_tree)
print(result)
# Generator time: 34.9485 seconds