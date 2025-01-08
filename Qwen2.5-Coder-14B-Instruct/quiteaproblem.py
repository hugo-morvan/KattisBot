import sys

def check_for_problem():
    for line in sys.stdin:
        if 'problem' in line.lower():
            print("yes")
        else:
            print("no")

check_for_problem()
# Generator time: 7.2634 seconds