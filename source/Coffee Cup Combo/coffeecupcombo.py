n = int(input())
s = input()

# Initialize variables
coffee_cups = 2
wake_up_count = 0

# Iterate through each lecture
for i in range(n):
    if s[i] == '1':
        # If there's a coffee machine, Jonna can stay awake
        wake_up_count += 1
    else:
        # If there's no coffee machine, check if she has enough coffee cups
        if coffee_cups > 0:
            wake_up_count += 1
            coffee_cups -= 1
        else:
            # If she doesn't have enough coffee cups, she can't stay awake
            break

print(wake_up_count)