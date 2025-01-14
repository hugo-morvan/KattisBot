 first_time = input()
now = input()
first_hour, first_minute = map(int, (fist_time).split(":"))
now_hour, now_minute=map(int,(now).split(":" )) 
if first_hour>23:
    if second<60 and fist_minut-15>=second : print((first_hour*4)+ (fist_minute-(first_minute)))   #when she checks the time in middle of minute format(i.e, less than 9 minutes remaining) or after that i mean morethan equal to nine min
elif fist_minut-15<second : print((23*4)+ (60+fist_hour)-(now_minute)) #when she checks the time just before end of hour(i.e, 9 minutes remaining) or after that i mean lessthan equal to nine min
elif fist_minut-15>second : print((first_hour*4)+ (60+fist_minute)-(now_minute)) #when she checks the time more than half an hour(i.e, 9 minutes remaining) or lessthan that i mean lessthan nine min
else:print("error")
# Generator time: 8.2860 seconds