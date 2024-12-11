import math
from fractions import Fraction

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def calculate_turns(radii):
    # Calculate the LCM of all radii
    lcm_value = radii[0]
    for radius in radii[1:]:
        lcm_value = lcm(lcm_value, radius)
    
    # Calculate the number of turns for each ring
    turns = [lcm_value // radius for radius in radii]
    
    # Simplify the fractions
    simplified_turns = [Fraction(turn).limit_denominator() for turn in turns]
    
    return simplified_turns

# Read input
N = int(input())
radii = list(map(int, input().split()))

# Calculate and print the turns
turns = calculate_turns(radii)
for turn in turns:
    print(turn)