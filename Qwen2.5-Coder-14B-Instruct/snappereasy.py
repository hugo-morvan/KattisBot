def snap_light(N, K):
    snappers = [False] * N  # All Snappers are initially OFF
    for _ in range(K):
        for i in range(N):
            if snappers[i]:
                snappers[i] = False
            else:
                snappers[i] = True
                if i < N - 1:
                    snappers[i + 1] = not snappers[i + 1]
    return "ON" if snappers[-1] else "OFF"

T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    result = snap_light(N, K)
    print(f"Case #{case}: {result}")
# Generator time: 22.7776 seconds