# Read the number of guests
n = int(input())

# Initialize variables to keep track of the maximum enjoyment and the corresponding guest
max_enjoyment = -1
most_fun_guest = ""

# Iterate through each guest's gift
for _ in range(n):
    # Read the guest's name and their enjoyment level
    guest_name, enjoyment_level = input().split()
    enjoyment_level = int(enjoyment_level)
    
    # Check if this gift is the most fun one so far
    if enjoyment_level > max_enjoyment:
        max_enjoyment = enjoyment_level
        most_fun_guest = guest_name

# Print the name of the guest with the most fun gift
print(most_fun_guest)