def max_enclosed_rectangle(A, B, C, D):
    # Calculate all possible rectangles
    rectangles = [
        (A, B), (A, C), (A, D),
        (B, C), (B, D),
        (C, D)
    ]
    
    # Calculate the area of each rectangle
    areas = [a * b for a, b in rectangles]
    
    # Return the maximum area
    return max(areas)

# Read input
A, B, C, D = map(int, input().split())

# Calculate and print the result
print(max_enclosed_rectangle(A, B, C, D))