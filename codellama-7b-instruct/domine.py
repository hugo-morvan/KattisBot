import sys
def main(N, K):
    # Initialize a 2D array that will store the values in each row
    board = []
    for i in range(0, N):
        board.append([])
        for j in range(0, 3):
            board[i].append(int(sys.stdin.readline()))
    
    # Initialize a variable that will store the maximum sum possible
    maxSum = -1

    def is_row_covered(x):
        # Check if row x is completely covered
        for i in range(0, N):
            for j in range(0, 3):
                # Check if a domino exists on the current field
                if board[i][j] == x:
                    return False
        
        return True
    
    def is_col_covered(x):
        # Check if column x is completely covered
        for i in range(0, N):
            for j in range(0, 3):
                # Check if a domino exists on the current field
                if board[i][j] == x:
                    return False
        
        return True
    
    def is_diagonal_covered(x):
        # Check if diagonal x is completely covered
        for i in range(0, N):
            for j in range(0, 3):
                # Check if a domino exists on the current field
                if board[i][j] == x:
                    return False
        
        return True
    
    def is_covered():
        # Check if the whole board is covered by dominoes
        for i in range(0, N):
            for j in range(0, 3):
                # Check if a domino exists on the current field
                if board[i][j] == 0:
                    return False
        
        return True
    
    def cover_row(x):
        # Cover all of row x with dominoes
        for i in range(0, N):
            for j in range(0, 3):
                if board[i][j] == x:
                    # Cover the current field with a domino
                    board[i][j] = -1
    
    def cover_col(x):
        # Cover all of column x with dominoes
        for i in range(0, N):
            for j in range(0, 3):
                if board[i][j] == x:
                    # Cover the current field with a domino
                    board[i][j] = -1
    
    def cover_diagonal(x):
        # Cover all of diagonal x with dominoes
        for i in range(0, N):
            for j in range(0, 3):
                if board[i][j] == x:
                    # Cover the current field with a domino
                    board[i][j] = -1
    
    def cover_board():
        # Initialize all fields of the board to be covered
        for i in range(0, N):
            for j in range(0, 3):
                board[i][j] = -1
    
    while not is_covered() and K > 0:
        # If there are dominoes left but the whole board isn't covered yet
        
        if is_row_covered(2) or is_col_covered(2) or is_diagonal_covered(2):
            # If row, column, or diagonal 2 is completely covered with dominoes
            
            if maxSum < sum([board[i][j] for i in range(0, N) for j in range(0, 3)]):
                # Update the maximum sum possible
                maxSum = sum([board[i][j] for i in range(0, N) for j in range(0, 3)])
        
        else:
            if not is_row_covered(1) and not is_col_covered(1) and not is_diagonal_covered(1):
                # If row, column, or diagonal 1 isn't completely covered with dominoes
                
                cover_row(2)
                K -= 1
            
            elif not is_row_covered(3) and not is_col_covered(3) and not is_diagonal_covered(3):
                # If row, column, or diagonal 3 isn't completely covered with dominoes
                
                cover_col(2)
                K -= 1
            
            elif not is_row_covered(5) and not is_col_covered(5) and not is_diagonal_covered(5):
                # If row, column, or diagonal 5 isn't completely covered with dominoes
                
                cover_diagonal(2)
                K -= 1
            
            else:
                # If there aren't any dominoes left that can be used to cover the whole board
                
                cover_board()
    
    if maxSum < sum([board[i][j] for i in range(0, N) for j in range(0, 3)]):
        # If there is a greater sum possible with more dominoes used
        
        maxSum = sum([board[i][j] for i in range(0, N) for j in range(0, 3)])
    
    print(maxSum)
    
main(int(sys.stdin.readline()), int(sys.stdin.readline()))
# Generator time: 29.1792 seconds