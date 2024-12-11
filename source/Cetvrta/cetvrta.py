def find_fourth_vertex():
    # Read the coordinates of the three points
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Calculate the fourth vertex based on the properties of a rectangle
    if x1 == x2:
        x4 = x3
        y4 = y1
    elif y1 == y2:
        x4 = x1
        y4 = y3
    else:
        raise ValueError("The given points do not form a rectangle.")

    # Print the coordinates of the fourth vertex
    print(x4, y4)

# Call the function to find and print the fourth vertex
find_fourth_vertex()