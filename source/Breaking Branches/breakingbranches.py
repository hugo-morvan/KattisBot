def bob_and_alice_pastime(n):
    # Check if the length of the branch is odd
    if n % 2 == 1:
        # Bob wins if the length is odd
        return "Bob"
    else:
        # Alice wins if the length is even
        # Alice's optimal move is to break the branch into two equal parts
        return "Alice", n // 2

# Read input
n = int(input())

# Determine the winner and Alice's optimal move
winner, move = bob_and_alice_pastime(n)

# Print the result
print(winner)
if winner == "Alice":
    print(move)