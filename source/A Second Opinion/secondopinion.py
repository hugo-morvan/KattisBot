s = int(input())
hours = s // 3600
minutes = (s % 3600) // 60
seconds = s % 60
print(f"{hours} : {minutes} : {seconds}")