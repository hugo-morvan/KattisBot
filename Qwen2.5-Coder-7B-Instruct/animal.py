def parse_tree(tree_str):
    stack = []
    current_node = []
    for char in tree_str:
        if char == '(':
            stack.append(current_node)
            current_node = []
        elif char == ')':
            parent = stack.pop()
            parent.append(tuple(sorted(current_node)))
            current_node = parent
        elif char == ',':
            continue
        else:
            current_node.append(int(char))
    return tuple(sorted(current_node))

def count_common_groups(alice_tree, bob_tree):
    alice_set = set(alice_tree)
    bob_set = set(bob_tree)
    common_groups = alice_set.intersection(bob_set)
    return len(common_groups)

def main():
    N = int(input())
    alice_tree_str = input().strip()
    bob_tree_str = input().strip()

    alice_tree = parse_tree(alice_tree_str)
    bob_tree = parse_tree(bob_tree_str)

    result = count_common_groups(alice_tree, bob_tree)
    print(result)

if __name__ == "__main__":
    main()
# Generator time: 8.1701 seconds