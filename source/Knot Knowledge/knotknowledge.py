# Read the number of knots Sonja needs to learn
n = int(input())

# Read the list of knots Sonja needs to learn
need_to_learn = list(map(int, input().split()))

# Read the list of knots Sonja has learned so far
learned = list(map(int, input().split()))

# Find the remaining knot
remaining_knot = (set(need_to_learn) - set(learned)).pop()

# Output the remaining knot
print(remaining_knot)