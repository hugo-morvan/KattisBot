import math

def initial_area(n, l):
    return (n * l**2) / (4 * math.tan(math.pi / n))

def area_after_land_grab(n, l, d):
    # Calculate the area of the new regular n-gon after the land grab
    new_l = l + d
    return (n * new_l**2) / (4 * math.tan(math.pi / n))

def main():
    N = int(input())
    results = []

    for _ in range(N):
        n, l, d, g = map(int, input().split())
        
        # Initial area of the regular n-gon
        current_area = initial_area(n, l)
        
        # Calculate the area after each land grab
        for _ in range(g):
            current_area = area_after_land_grab(n, l, d)
        
        # Add the result to the list
        results.append(current_area)

    # Output the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 23.9701 seconds