# Read the input values
n, m = map(int, input().split())
monday_attendance = set(map(int, input().split()))
tuesday_attendance = set(map(int, input().split()))

# Find the intersection of the two sets
common_students = monday_attendance & tuesday_attendance

# Print the common students in the order they appear on the second line
for student in monday_attendance:
    if student in common_students:
        print(student, end=' ')
print()