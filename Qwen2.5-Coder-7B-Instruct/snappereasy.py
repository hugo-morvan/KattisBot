def snapper_light_state(T):
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        if N == 1:
            result = "ON" if K % 2 == 0 else "OFF"
        else:
            result = "ON" if (K // (N - 1)) % 2 == 0 else "OFF"
        print(f"Case #{t}: {result}")

# Example usage
T = int(input())
snapper_light_state(T)
# Generator time: 5.3998 seconds