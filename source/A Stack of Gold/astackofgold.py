def find_gold_stack(w, s):
    # Calculate the number of coins being weighed
    c = s * (s + 1) // 2
    
    # Calculate the difference between the reported weight and the expected weight for a stack of tungsten coins
    diff = w - (29260 * c)
    
    # Determine which stack has the gold coins
    stack_with_gold = 1 + (diff // 110)
    
    print(stack_with_gold)

# Read input
w, s = map(int, input().split())

# Find and print the stack with the gold coins
find_gold_stack(w, s)