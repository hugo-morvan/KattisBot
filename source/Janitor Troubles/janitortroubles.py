import math

def max_quadrilateral_area(s1, s2, s3, s4):
    # Check if the given side lengths can form a quadrilateral
    if not (2 * min(s1, s2, s3, s4) < s1 + s2 + s3 + s4):
        return 0

    # Function to calculate the area of a quadrilateral using Brahmagupta's formula
    def heron(a, b, c, d):
        s = (a + b + c + d) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d))

    # Try all possible combinations of the sides
    areas = []
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                l = 4 - i - j - k
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    area = heron(s1, s2, s3, s4)
                    areas.append(area)

    # Return the maximum area found
    return max(areas)

# Read input
s1, s2, s3, s4 = map(int, input().split())

# Calculate and print the maximum area
print(max_quadrilateral_area(s1, s2, s3, s4))