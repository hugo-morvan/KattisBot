# Read the initial time from the first line
initial_time = input()

# Read the current time from the second line
current_time = input()

# Split the times into hours and minutes
initial_hours, initial_minutes = map(int, initial_time.split(':'))
current_hours, current_minutes = map(int, current_time.split(':'))

# Calculate the total minutes passed since the initial time
total_minutes_passed = (current_hours * 60 + current_minutes) - (initial_hours * 60 + initial_minutes)

# Print the result
print(total_minutes_passed)
# Generator time: 5.8305 seconds