n = int(input())
dna_strand = input()
mutations = 0
for i in range(n):
    if dna_strand[i] == 'A' and dna_strand[i + 1] == 'B':
        mutations += 1
    elif dna_strand[i] == 'B' and dna_strand[i + 1] == 'A':
        mutations += 1
print(mutations)
# Generator time: 4.7250 seconds