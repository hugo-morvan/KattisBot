import math

# Read the coordinates of the vertices of the triangle
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())

# Read the number of apple trees
N = int(input())

# Function to calculate the area of a triangle given its vertices
def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

# Calculate the area of the triangle formed by the vertices
triangle_area_value = triangle_area(Ax, Ay, Bx, By, Cx, Cy)

# Initialize variables to count the number of trees inside the triangle
inside_count = 0

# Read the coordinates of each apple tree
for _ in range(N):
    tx, ty = map(int, input().split())
    
    # Check if the apple tree is inside the triangle
    if (tx >= min(Ax, Bx, Cx) and tx <= max(Ax, Bx, Cx) and
        ty >= min(Ay, By, Cy) and ty <= max(Ay, By, Cy)):
        inside_count += 1

# Output the area of land belonging to Ante
print(f"{triangle_area_value:.1f}")

# Output the number of trees belonging to Ante
print(inside_count)