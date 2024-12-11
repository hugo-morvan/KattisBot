import sys

def calculate_square_corners(x, y, r):
    # Calculate the side length of the square
    side_length = 2 * r
    
    # Calculate the coordinates of the corners
    corners = [
        (x - r, y + r),
        (x + r, y + r),
        (x + r, y - r),
        (x - r, y - r)
    ]
    
    return corners

def main():
    # Read input
    x, y = map(int, input().split())
    r = int(input())
    
    # Calculate the corners of the square
    corners = calculate_square_corners(x, y, r)
    
    # Print the corners
    for corner in corners:
        print(*corner)

if __name__ == "__main__":
    main()