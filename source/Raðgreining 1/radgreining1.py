from collections import defaultdict

def piece_dna_sequence(n, m, sections):
    # Initialize a dictionary to store the positions and sequences
    pos_to_seq = defaultdict(str)
    
    # Process each section
    for s, seq in sections:
        pos_to_seq[s] = seq
    
    # Try to piece together the DNA sequence
    dna_sequence = []
    for i in range(1, n + 1):
        if i in pos_to_seq:
            dna_sequence.append(pos_to_seq[i])
        else:
            dna_sequence.append('?')
    
    # Check for contradictions
    for i in range(1, n + 1):
        if i not in pos_to_seq:
            continue
        for j in range(i + 1, n + 1):
            if j not in pos_to_seq:
                continue
            if pos_to_seq[i][-1] != pos_to_seq[j][0]:
                return "Villa"
    
    # Join the sequence and print the result
    return ''.join(dna_sequence)

# Read input
n, m = map(int, input().split())
sections = [tuple(map(int, input().split())) for _ in range(m)]

# Get the DNA sequence
dna_sequence = piece_dna_sequence(n, m, sections)

# Print the result
print(dna_sequence)