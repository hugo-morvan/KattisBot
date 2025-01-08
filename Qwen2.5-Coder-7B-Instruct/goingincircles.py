def find_train_carriages():
    s = int(input())  # Initial state of the light switch
    n = 3  # Start with the minimum number of carriages

    while True:
        print(f"? right", flush=True)
        next_s = int(input())
        if next_s != s:
            break
        n += 1

    print(f"? left", flush=True)
    last_s = int(input())

    if last_s == s:
        n += 1

    print(f"! {n}", flush=True)

find_train_carriages()
# Generator time: 5.5598 seconds