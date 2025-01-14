import itertools
import sys
if __name__ == "__main__":
    n = int(raw_input())
    staff = itertools.cycle(sys.stdin.readline().strip().split())
    for _ in range(n):
        print next(staff)
# Generator time: 4.1888 seconds