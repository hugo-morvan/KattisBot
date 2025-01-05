from math import gcd

def count_cp_sequences(S):
    def is_valid_sequence(sequence):
        if len(sequence) == 1:
            return True
        
        ratio = sequence[1] / sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] / sequence[i - 1] != ratio:
                return False
            if gcd(sequence[i], sequence[i - 1]) != 1:
                return False
        return True

    def find_sequences(S, current_sequence, index):
        if sum(current_sequence) == S:
            if is_valid_sequence(current_sequence):
                sequences.append(current_sequence[:])
            return
        if sum(current_sequence) > S or index >= len(numbers):
            return

        for i in range(index, len(numbers)):
            current_sequence.append(numbers[i])
            find_sequences(S, current_sequence, i + 1)
            current_sequence.pop()

    numbers = list(range(1, S + 1))
    sequences = []
    find_sequences(S, [], 0)

    return len(sequences)

t = int(input())
results = []

for _ in range(t):
    S = int(input())
    results.append(count_cp_sequences(S))

print(" ".join(map(str, results)))
# Generator time: 14.5155 seconds