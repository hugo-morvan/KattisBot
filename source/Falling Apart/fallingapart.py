To solve this problem, we need to determine how Alice and Bob can split the $n$ pieces of the integer optimally, such that one of them gets the maximum possible sum. This is a classic problem that can be solved using dynamic programming.

Here's a step-by-step approach to solve it:

1. **Understand the Problem**: Alice and Bob take turns picking pieces from the list. Alice goes first, and both players play optimally. The goal is to maximize the sum of the pieces each person gets.

2. **Dynamic Programming Approach**:
   - Let `dp[i][j]` represent the maximum sum Alice can get if she starts playing from index `i` and Bob plays optimally from index `j`.
   - The base case is when there are no more pieces left (`i > j`), in which case the sum is 0.
   - For each piece, Alice has two choices:
     - Pick the current piece and add it to her total, then let Bob play optimally from the next piece (`dp[i+1][j]`).
     - Skip the current piece and let Bob play optimally from the same piece (`dp[i+1][j-1]`).

3. **Calculate the Maximum Sum**:
   - Initialize `dp` table with zeros.
   - Fill the `dp` table using the recurrence relation.

4. **Output the Result**:
   - The result will be stored in `dp[0][n-1]`, which represents the maximum sum Alice can get if she starts from the first piece and Bob plays optimally from the last piece.

Here's the Python code implementing this approach:

```python
def max_sum_of_pieces(n, pieces):
    # Initialize the dp table
    dp = [[0] * n for _ in range(n)]
    
    # Fill the dp table
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            # Alice's choice: pick the current piece or skip it
            dp[i][j] = max(pieces[i] + dp[i+1][j], dp[i+1][j-1])
    
    # The result is stored in dp[0][n-1]
    return dp[0][n-1]

# Read input
n = int(input())
pieces = list(map(int, input().split()))

# Calculate the maximum sum
alice_sum = max_sum_of_pieces(n, pieces