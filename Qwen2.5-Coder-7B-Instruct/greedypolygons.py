import math

def calculate_area(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

def main():
    N = int(input())
    results = []
    
    for _ in range(N):
        n, l, d, g = map(int, input().split())
        
        # Calculate the initial area of the regular n-gon
        initial_area = calculate_area(n, l)
        
        # Each land grab increases the side length by 2 * d
        final_side_length = l + 2 * d * g
        
        # Calculate the area after g land grabs
        final_area = calculate_area(n, final_side_length)
        
        results.append(final_area)
    
    for result in results:
        print(f"{result:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 7.1403 seconds