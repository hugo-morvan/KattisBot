def max_domino_sum(N, K):
    # Read the chessboard
    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    # Calculate the maximum sum for each cell
    max_sums = [[0] * 3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            if j == 0:
                # Horizontal placement
                max_sums[i][j] = board[i][j] + board[i][j+1]
            elif j == 1:
                # Vertical placement
                max_sums[i][j] = board[i][j] + board[i+1][j]
            else:
                # Diagonal placement (if needed)
                max_sums[i][j] = board[i][j] + board[i+1][j+1]
    
    # Flatten the list of lists into a single list
    max_sums_flat = [max_sums[i][j] for i in range(N) for j in range(3)]
    
    # Sort cells by maximum sum in descending order
    max_sums_flat.sort(reverse=True)
    
    # Initialize the total sum
    total_sum = 0
    
    # Place K dominoes
    for i in range(K):
        total_sum += max_sums_flat[i]
    
    # Output the result
    print(total_sum)

# Read input
N, K = map(int, input().split())
max_domino_sum(N, K)
# Generator time: 29.5973 seconds