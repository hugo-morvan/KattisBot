# Read input values
a, b, c, d, e = map(int, input().split())
score = int(input())

# Determine the grade based on the score
if score >= e:
    grade = 'E'
elif score >= d:
    grade = 'D'
elif score >= c:
    grade = 'C'
elif score >= b:
    grade = 'B'
elif score >= a:
    grade = 'A'
else:
    grade = 'F'

# Output the grade
print(grade)