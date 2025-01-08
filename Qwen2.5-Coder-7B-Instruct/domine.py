def max_sum_with_dominoes(N, K, board):
    # Create a list to store the maximum sums for each column combination
    dp = [[0] * 8 for _ in range(K + 1)]
    
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(i + 1, N):
                # Calculate the sum of the current two rows and the maximum sums from previous states
                dp[k][((board[i][0] + board[j][0]) % 8) * 4 + ((board[i][1] + board[j][1]) % 8)] = max(dp[k][((board[i][0] + board[j][0]) % 8) * 4 + ((board[i][1] + board[j][1]) % 8)], dp[k-1][(board[i][2] + board[j][2]) % 8])
                dp[k][((board[i][1] + board[j][1]) % 8) * 4 + ((board[i][0] + board[j][0]) % 8)] = max(dp[k][((board[i][1] + board[j][1]) % 8) * 4 + ((board[i][0] + board[j][0]) % 8)], dp[k-1][(board[i][2] + board[j][2]) % 8])
                dp[k][((board[i][2] + board[j][2]) % 8) * 4 + ((board[i][1] + board[j][1]) % 8)] = max(dp[k][((board[i][2] + board[j][2]) % 8) * 4 + ((board[i][1] + board[j][1]) % 8)], dp[k-1][(board[i][0] + board[j][0]) % 8])
                dp[k][((board[i][2] + board[j][2]) % 8) * 4 + ((board[i][0] + board[j][0]) % 8)] = max(dp[k][((board[i][2] + board[j][2]) % 8) * 4 + ((board[i][0] + board[j][0]) % 8)], dp[k-1][(board[i][1] + board[j][1]) % 8])
    
    # Find the maximum sum possible with exactly K dominoes
    max_sum = 0
    for i in range(8):
        for j in range(8):
            max_sum = max(max_sum, dp[K][i * 4 + j] + board[N-1][i] + board[N-1][j])
    
    return max_sum

# Input reading
N = int(input())
K = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# Output the result
print(max_sum_with_dominoes(N, K, board))
# Generator time: 17.2587 seconds