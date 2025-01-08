def time_difference(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    
    total_start_minutes = start_hour * 60 + start_minute
    total_end_minutes = end_hour * 60 + end_minute
    
    difference = total_end_minutes - total_start_minutes
    
    return difference

start_time = input()
end_time = input()

print(time_difference(start_time, end_time))
# Generator time: 14.7243 seconds