def stopwatch_timer(N, presses):
    timer = 0
    is_running = False

    for press in presses:
        if is_running:
            timer += 1
            if timer == press:
                is_running = False
        else:
            if press == 0:
                is_running = True
            elif press > timer:
                is_running = True
                timer = press

    if is_running:
        return "still running"
    else:
        return timer

# Read input
N = int(input())
presses = [int(input()) for _ in range(N)]

# Calculate and print output
result = stopwatch_timer(N, presses)
print(result)