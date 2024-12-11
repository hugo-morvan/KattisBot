def check_drawing(drawing):
    # Split the drawing into parts
    parts = drawing.split('|')
    
    # Count the number of vertical bars on each side of the eye
    left_bars = parts[0].count('|')
    right_bars = parts[-1].count('|')
    
    # Check if the number of bars on both sides is equal
    if left_bars == right_bars:
        return "correct"
    else:
        return "fix"

# Read input
drawing = input()

# Check the drawing and print the result
result = check_drawing(drawing)
print(result)