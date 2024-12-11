n = int(input())
correct_answers = [input() for _ in range(n)]
hanh_answers = [None] * n

for i in range(n):
    hanh_answers[i] = input()

score = sum(1 for c, h in zip(correct_answers, hanh_answers) if c == h)

print(score)