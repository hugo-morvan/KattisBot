def can_square_fit_in_circle(L, R):
    # Calculate the diagonal of the square
    diagonal = L * (2 ** 0.5)
    
    # Check if the diagonal of the square is less than or equal to the diameter of the circle
    if diagonal <= 2 * R:
        return "fits"
    else:
        return "nope"

# Read input values
L, R = map(int, input().split())

# Determine if the square can fit in the circle
result = can_square_fit_in_circle(L, R)

# Print the result
print(result)