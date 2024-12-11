def count_valid_buttons(N):
    valid_buttons = 0
    for _ in range(N):
        button_name = input()
        if "pink" in button_name.lower() or "rose" in button_name.lower():
            valid_buttons += 1
    if valid_buttons == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(valid_buttons)

# Read the number of button packages
N = int(input())
count_valid_buttons(N)