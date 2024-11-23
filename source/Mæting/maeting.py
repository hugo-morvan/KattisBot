
    # Read input values
n, m = map(int, input().split())
monday_attendance = set(map(int, input().split()))
tuesday_attendance = set(map(int, input().split()))

# Find common students
common_students = monday_attendance.intersection(tuesday_attendance)

# Print the result in the required order
for student in sorted(monday_attendance):
    if student in common_students:
        print(student)
    