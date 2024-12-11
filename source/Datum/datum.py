def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def zellers_congruence(day, month, year):
    """Calculate the day of the week using Zeller's Congruence."""
    if month < 3:
        month += 12
        year -= 1
    
    k = day
    j = year // 100
    h = (k + 13 * (month + 1) // 5 + j + j // 4 + i // 4 - 2 * j) % 7
    
    # Convert the result to a day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[h]

# Read input
D, M = map(int, input().split())

# Calculate the day of the week
day_of_week = zellers_congruence(D, M, 2009)

# Output the result
print(day_of_week)