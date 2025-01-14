W, H, K = map(int, input().split())
live_points = set()
for i in range(K):
    x, y = map(int, input().split())
    live_points.add((x, y))

max_rhombinoes = 0
for i in range(W * H - len(live_points)):
    for j in range(i + 1, W * H - len(live_points)):
        if (i % W == j % W) or ((i // W) == (j // W)):
            continue
        max_rhombinoes += 1
print(max_rhombinoes)
# Generator time: 5.8451 seconds