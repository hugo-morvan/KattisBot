def max_bishops_on_chessboard(N):
    # A bishop can only threaten another bishop if they are on the same diagonal.
    # Therefore, we can place a bishop on every square of one color (either black or white) in the chessboard.
    # Since a standard chessboard has an equal number of black and white squares, we can place at most N bishops.
    return N

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each chessboard size
output = []
for i in range(1, len(data)):
    N = int(data[i])
    result = max_bishops_on_chessboard(N)
    output.append(str(result))

# Print results
print("\n".join(output))
# Generator time: 6.2660 seconds