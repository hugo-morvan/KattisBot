# Read input
N = int(input())
K = int(input())
turns = [input().split() for _ in range(K)]

# Initialize a set to keep track of face-down cards
face_down_cards = set(range(1, N + 1))

# Process each turn and update the state of the game
for C1, C2, P1, P2 in turns:
    if P1 == P2:
        # If the pictures match, remove both cards from the set
        face_down_cards.discard(int(C1))
        face_down_cards.discard(int(C2))

# Calculate the number of matching pairs that can be scored with certainty
S = (N - len(face_down_cards)) // 2

# Output the result
print(S)
# Generator time: 6.4226 seconds