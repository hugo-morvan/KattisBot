# Read input
k = int(input())
your_answers = input()
friend_answers = input()

# Calculate the maximum possible score
max_score = k + sum(1 for a, b in zip(your_answers, friend_answers) if a == b)

# Output the result
print(max_score)
# Generator time: 13.0883 seconds