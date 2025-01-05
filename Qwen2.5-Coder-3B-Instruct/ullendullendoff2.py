def find_valid_order(staff_members):
    # Identify the relative
    relative = staff_members[0]
    
    # Function to simulate the mantra and check if the relative is picked last
    def is_valid_order(order):
        current_index = order.index(relative)
        for _ in range(len(order) - 1):
            current_index = (current_index + 1) % len(order)
            if order[current_index] == relative:
                return False
        return True
    
    # Try all possible starting points
    for start in range(len(staff_members)):
        if is_valid_order(staff_members[start:] + staff_members[:start]):
            return staff_members[start:] + staff_members[:start]
    
    return None

# Read input
n = int(input())
staff_members = [input() for _ in range(n)]

# Find and print the valid order
valid_order = find_valid_order(staff_members)
if valid_order:
    print('\n'.join(valid_order))
else:
    print("No valid order found")
# Generator time: 21.9997 seconds