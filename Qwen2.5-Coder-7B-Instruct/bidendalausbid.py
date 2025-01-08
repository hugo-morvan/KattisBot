from datetime import datetime

# Read input times
first_time = input()
current_time = input()

# Convert string times to datetime objects
first_dt = datetime.strptime(first_time, "%H:%M")
current_dt = datetime.strptime(current_time, "%H:%M")

# Calculate the time difference in minutes
time_difference = (current_dt - first_dt).total_seconds() / 60

# Print the number of minutes Svala has waited
print(int(time_difference))
# Generator time: 4.6777 seconds