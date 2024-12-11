# Read input values
a, b = map(int, input().split())
recipe1 = []
recipe2 = []

# Read ingredients for the first shot
for _ in range(a):
    v, c = map(int, input().split())
    recipe1.append((v, c))

# Read ingredients for the second shot
for _ in range(b):
    v, c = map(int, input().split())
    recipe2.append((v, c))

# Calculate total alcohol content for the first shot
total_alcohol1 = sum(v * c / 100 for v, c in recipe1)

# Calculate total alcohol content for the second shot
total_alcohol2 = sum(v * c / 100 for v, c in recipe2)

# Compare alcohol contents
if total_alcohol1 == total_alcohol2:
    print("same")
else:
    print("different")