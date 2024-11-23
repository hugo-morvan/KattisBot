def check_attendance_list():
    n, r, c = map(int, input().split())
    rows = [input().split() for _ in range(r)]
    attendance_list = input().split()

    results = []
    for i in range(r):
        current_row = rows[i]
        if current_row == attendance_list[:c]:
            results.append("left")
        elif current_row == attendance_list[-c:]:
            results.append("right")
        else:
            results.append("unknown")

    print("\n".join(results))

check_attendance_list()