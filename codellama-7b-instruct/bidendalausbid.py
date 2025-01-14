first_time = input()
current_time = input()
hours, minutes = current_time.split(':')
minutes = int(minutes)
hours = int(hours)
if hours > 23 or hours < 0:
    print("error")
else:
    first_hour, first_minute = first_time.split(':')
    first_minute = int(first_minute)
    first_hour = int(first_hour)
    if minutes >= first_minute and hours == first_hour:
        print("0")
    else:
        difference_in_minutes = abs(minutes - first_minute)
        difference_in_hours = abs(hours - first_hour)
        total_waiting_time = (difference_in_minutes + 60 * difference_in_hours) % 1440
        print(total_waiting_time)
# Generator time: 9.2192 seconds