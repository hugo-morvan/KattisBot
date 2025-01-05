def find_triple_correlation(sequence):
    # Convert the sequence into a list of integers
    digits = list(map(int, sequence.split()))
    
    # Number of digits in the sequence
    p = len(digits)
    
    # Iterate over all possible triples in the sequence
    for i in range(p - 2):
        a = digits[i]
        b = digits[i + 1]
        c = digits[i + 2]
        
        # Check the first condition: a followed by b followed by c
        if (i + 2 < p and digits[i + 2] == c):
            # Check if there is a c at position i + m after b
            for m in range(1, p - i - 1):
                if (i + m + 1 < p and digits[i + m + 1] == c):
                    break
            else:
                continue
        
        # Check the second condition: b followed by c followed by a
        if (i + 1 < p and digits[i + 1] == b):
            # Check if there is an a at position i + n before b
            for n in range(1, i + 1):
                if (i - n >= 0 and digits[i - n] == a):
                    break
            else:
                continue
        
        # Check the third condition: a followed by b followed by c
        if (i + 2 < p and digits[i + 2] == c):
            # Check if there is a b at position i + n after a
            for n in range(1, p - i - 1):
                if (i + n + 1 < p and digits[i + n + 1] == b):
                    break
            else:
                continue
        
        # If all conditions are satisfied, we have found a triple correlation
        return f"{a}({i}){b}({i + 1}){c}({i + 2})"
    
    # If no triple correlation is found, return "random sequence"
    return "random sequence"

# Read input
p = int(input())
sequence = input()

# Find and print the triple correlation
print(find_triple_correlation(sequence))
# Generator time: 32.8487 seconds