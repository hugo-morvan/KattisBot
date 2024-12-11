from itertools import combinations

def find_legit_dwarves():
    # Read input numbers
    numbers = [int(input()) for _ in range(9)]
    
    # Iterate over all combinations of 7 numbers from the 9
    for combo in combinations(numbers, 7):
        if sum(combo) == 100:
            # Print the combination
            print(*combo)
            return

# Call the function to find and print the legit dwarves
find_legit_dwarves()