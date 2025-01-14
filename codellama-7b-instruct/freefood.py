def solve(s_i, t_i):
    return (t_i - s_i + 1)
N = int(input())
print(sum([solve(*map(int, input().split())) for _ in range(N)]))
# Generator time: 4.0862 seconds