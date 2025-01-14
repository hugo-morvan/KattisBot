def solve(first_map, second_map):
    first_map = list(filter(lambda x: len(x) > 0 and not x[0] == '?', first_map))
    second_map = list(filter(lambda x: len(x) > 0 and not x[0] == '?', second_map))

    n = len(first_map)
    m = len(second_map)

    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(0, n + 1):
        dp[i][0] = True

    for j in range(1, m + 1):
        dp[0][j] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_map[i - 1][1:] == second_map[j - 1][1:]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return sum(dp[-1])
# Generator time: 8.5429 seconds