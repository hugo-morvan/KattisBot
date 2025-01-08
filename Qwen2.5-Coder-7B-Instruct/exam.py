k = int(input())
my_answers = input()
friend_answers = input()

# Calculate the number of correct answers in my friend's exam
friend_correct = sum(1 for a, b in zip(friend_answers, friend_answers) if a == b)

# The maximum possible score I could have gotten
max_score = min(k + (len(my_answers) - k), len(my_answers))

print(max_score)
# Generator time: 4.3330 seconds