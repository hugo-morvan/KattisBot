def find_box_holder(initial_player, num_questions, questions):
    current_player = initial_player
    for _, answer in questions:
        if answer == 'N':
            current_player = (current_player + 1) % 8
        elif answer == 'P':
            continue
        else:
            current_player = (current_player - 1) % 8
    return current_player

# Read input
initial_player = int(input())
num_questions = int(input())
questions = [input().split() for _ in range(num_questions)]

# Find and print the final holder of the box
final_holder = find_box_holder(initial_player, num_questions, questions)
print(final_holder)