# Read the input string of moves
moves = input()

# Initialize the starting position of the ball
ball_position = 1

# Iterate through each move
for move in moves:
    # If the move is 'A', swap with the middle cup
    if move == 'A':
        ball_position = 2
    # If the move is 'B', swap with the right cup
    elif move == 'B':
        ball_position = 3
    # If the move is 'C', swap with the left cup
    elif move == 'C':
        ball_position = 1

# Output the final position of the ball
print(ball_position)