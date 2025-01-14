import sys
from collections import deque

def find_convex(n):
    # This function returns a list of points on the convex hull of the n given points
    if n == 1:
        return [(0, 0)]

    elif n == 2:
        return [(0, 0), (0, 1)]

    else:
        # first find a point on the convex hull that has lowest x coord and then lowest y coord
        points = []
        for i in range(n):
            if sys.stdin.readline().strip() == 'Y':
                points += [(i, 0)]
        if len(points) == 1:
            return [points[0]]

        # sort by y coordinate
        points = sorted(points, key=lambda p: p[1])

        # find the point with lowest x coord
        first_point = points[0][0]
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y':
                first_point = points[i + 1][0]
                break

        # find the point with lowest y coord and not equal to first point
        second_point = points[0][1]
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y' and points[i + 1][0] != first_point:
                second_point = points[i + 1][1]
                break

        # find the point that is not on the line connecting first and second point
        third_point = -1
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y' and points[i + 1][0] != first_point and points[i + 1][1] != second_point:
                third_point = points[i + 1][0]
                break

        # find the point that is not on the line connecting first, second, and third point
        fourth_point = -1
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y' and points[i + 1][0] != first_point and points[i + 1][1] != second_point and points[i + 1][0] != third_point:
                fourth_point = points[i + 1][1]
                break

        # return the convex hull as a list of tuples
        return [(first_point, second_point), (second_point, third_point), (third_point, fourth_point)]


def find_convex_hull(n):
    # This function returns the points on the convex hull of the n given points in counter-clockwise order
    if n == 1:
        return [(0, 0)]

    elif n == 2:
        return [(0, 0), (0, 1)]

    else:
        # first find a point on the convex hull that has lowest x coord and then lowest y coord
        points = []
        for i in range(n):
            if sys.stdin.readline().strip() == 'Y':
                points += [(i, 0)]
        if len(points) == 1:
            return [points[0]]

        # sort by y coordinate
        points = sorted(points, key=lambda p: p[1])

        # find the point with lowest x coord
        first_point = points[0][0]
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y':
                first_point = points[i + 1][0]
                break

        # find the point with lowest y coord and not equal to first point
        second_point = points[0][1]
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y' and points[i + 1][0] != first_point:
                second_point = points[i + 1][1]
                break

        # find the point that is not on the line connecting first and second point
        third_point = -1
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y' and points[i + 1][0] != first_point and points[i + 1][1] != second_point:
                third_point = points[i + 1][0]
                break

        # find the point that is not on the line connecting first, second, and third point
        fourth_point = -1
        for i in range(len(points) - 1):
            if sys.stdin.readline().strip() == 'Y' and points[i + 1][0] != first_point and points[i + 1][1] != second_point and points[i + 1][0] != third_point:
                fourth_point = points[i + 1][1]
                break

        # return the convex hull as a list of tuples
        return [(first_point, second_point), (second_point, third_point), (third_point, fourth_point)]


def solve():
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        points += [(int(sys.stdin.readline().split()[0]), int(sys.stdin.readline().split()[1]))]
    convex_hull = find_convex_hull(len(points))
    print(len(convex_hull))
    for i in range(len(convex_hull)):
        point = convex_hull[i]
        print("{} {}".format(point[0], point[1]))
    sys.exit()


solve()
# Generator time: 32.6141 seconds