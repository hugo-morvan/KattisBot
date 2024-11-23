def find_smiles(input_line):
    # Split the input line into individual characters
    chars = list(input_line)
    
    # Initialize a list to store the memory addresses of smiles
    smile_addresses = []
    
    # Iterate over the characters to find smile sequences
    for i in range(len(chars) - 3):
        # Check for the four possible smile sequences
        if chars[i] == ':' and chars[i+1] in [')', ';'] and chars[i+2] == ')' and chars[i+3] in [')', ';']:
            smile_addresses.append(i)
    
    # Print the memory addresses of the found smiles
    print(' '.join(map(str, smile_addresses)))

# Read input
input_line = input()

# Find and print the memory addresses of the smiles
find_smiles(input_line)