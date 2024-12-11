def maximize_robot_movement(N, sequence):
    # Find the last occurrence of 'R' in the sequence
    last_R_index = sequence.rfind('R')
    
    # If 'R' is not found, the robot cannot move to the right
    if last_R_index == -1:
        return 'B' * N
    
    # Calculate the number of commands needed to move to the right to the last 'R'
    commands_needed = len(sequence) - last_R_index - 1
    
    # Generate the sequence of commands
    commands = ['R'] * commands_needed + ['B'] * (N - commands_needed)
    
    return ''.join(commands)

# Read input
N = int(input())
sequence = input()

# Get the result and print it
result = maximize_robot_movement(N, sequence)
print(result)