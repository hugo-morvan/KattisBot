import math

def find_max_radius(R, l, w):
    return R - min(l / 2, w / 4)

def main():
    R = float(input())
    l = float(input())
    w = float(input())
    T = int(input())
    
    results = []
    for _ in range(T):
        A = float(input())
        B = float(input())
        r_max = find_max_radius(R, l, w)
        results.append(r_max)
    
    for result in results:
        print(f"{result:.5f}")

if __name__ == "__main__":
    main()
# Generator time: 5.5476 seconds