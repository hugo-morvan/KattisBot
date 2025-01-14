import sys

def get_input():
    return int(sys.stdin.readline())

def add(a, b):
    return a + b

if __name__ == '__main__':
    a = get_input()
    b = get_input()
    print(add(a,b))
# Generator time: 3.6942 seconds