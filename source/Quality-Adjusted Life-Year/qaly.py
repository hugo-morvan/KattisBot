N = int(input())
total_qaly = 0.0

for _ in range(N):
    q, y = map(float, input().split())
    total_qaly += q * y

print(f"{total_qaly:.3f}")