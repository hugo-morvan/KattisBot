# Read input values
x = int(input())
y = int(input())

# Determine the quadrant based on the signs of x and y
if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
else:
    quadrant = 4

# Output the quadrant number
print(quadrant)