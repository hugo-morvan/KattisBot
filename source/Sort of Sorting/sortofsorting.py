import sys

def sort_student_last_names():
    while True:
        n = int(input())
        if n == 0:
            break
        
        last_names = []
        for _ in range(n):
            last_names.append(input().strip())
        
        # Sort the last names based on the first two letters
        sorted_last_names = sorted(last_names, key=lambda x: x[:2])
        
        # Print the sorted last names
        for name in sorted_last_names:
            print(name)
        
        # Print a blank line between cases
        print()

# Read input from stdin and pass it to the function
sort_student_last_names()