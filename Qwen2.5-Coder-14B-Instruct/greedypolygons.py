import math

def polygon_area(n, side_length):
    return (n * side_length**2) / (4 * math.tan(math.pi / n))

def land_grab_area(n, side_length, d, g):
    if g == 0:
        return polygon_area(n, side_length)
    
    # Calculate the radius of the circumscribed circle
    R = side_length / (2 * math.sin(math.pi / n))
    
    # After one land grab, the new shape is a circle with radius R + d
    if g == 1:
        return math.pi * (R + d)**2
    
    # For more than one land grab, the area becomes a circle with radius R + g*d
    return math.pi * (R + g * d)**2

def main():
    N = int(input())
    results = []
    
    for _ in range(N):
        n, l, d, g = map(int, input().split())
        area = land_grab_area(n, l, d, g)
        results.append(area)
    
    for result in results:
        print(f"{result:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 34.5186 seconds