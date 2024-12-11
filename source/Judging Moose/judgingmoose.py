# Read input values
l, r = map(int, input().split())

# Determine the number of points based on the number of tines on the left and right
if l == 0 or r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l + r}")
else:
    print(f"Odd {max(l, r) * 2}")