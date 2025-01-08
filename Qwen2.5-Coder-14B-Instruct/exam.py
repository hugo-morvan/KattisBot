k = int(input())
my_answers = input().strip()
friend_answers = input().strip()

# Calculate the number of matching answers with the friend's correct answers
matching_with_correct = sum(1 for a, b in zip(my_answers, friend_answers) if a == b and b == 'T')

# Calculate the number of questions my friend got wrong
wrong_by_friend = len(friend_answers) - k

# The maximum score I could have is the sum of:
# 1. All the answers I got correct that matched with my friend's correct answers
# 2. The remaining correct answers from my friend that I could have gotten by answering incorrectly where they answered correctly
max_score = matching_with_correct + min(wrong_by_friend, k - matching_with_correct)

print(max_score)
# Generator time: 21.5554 seconds