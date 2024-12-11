def is_possible(a, b, c):
    # Check all possible operations
    if a + b == c:
        return True
    if a - b == c or b - a == c:
        return True
    if a * b == c:
        return True
    if a / b == c and b != 0:
        return True
    if b / a == c and a != 0:
        return True
    return False

def main():
    # Read the number of test cases
    N = int(input())
    
    # Process each test case
    for _ in range(N):
        a, b, c = map(int, input().split())
        if is_possible(a, b, c):
            print("Possible")
        else:
            print("Impossible")

if __name__ == "__main__":
    main()