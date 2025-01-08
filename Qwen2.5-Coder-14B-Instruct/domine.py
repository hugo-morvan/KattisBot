def max_sum_with_dominoes(N, K, board):
    # Initialize DP table
    dp = [[[float('-inf')] * 2 for _ in range(3)] for _ in range(K + 1)]
    
    # Base case: no dominoes placed
    for i in range(3):
        dp[0][i][0] = 0
    
    # Fill the DP table
    for k in range(1, K + 1):
        for j in range(N):
            for i in range(3):
                for l in range(3):
                    if (j == 0 and i != 0) or (i == 2 and l == 0):
                        continue
                    
                    # Place a vertical domino
                    if i == l:
                        dp[k][i][1] = max(dp[k][i][1], dp[k - 1][i][0] + board[j][i])
                    
                    # Place a horizontal domino
                    if (i, l) in [(0, 1), (1, 2), (0, 2)]:
                        dp[k][l][0] = max(dp[k][l][0], dp[k - 1][i][0] + board[j][i] + board[j][l])
    
    # Find the maximum sum
    max_sum = float('-inf')
    for i in range(3):
        for state in [0, 1]:
            max_sum = max(max_sum, dp[K][i][state])
    
    return max_sum

# Read input
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(max_sum_with_dominoes(N, K, board))
# Generator time: 48.5218 seconds