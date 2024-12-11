def can_build_closed_track(X, Y):
    if X == 0 and Y == 0:
        return "possible"
    elif X == 0 or Y == 0:
        return "impossible"
    else:
        return "possible"

# Read input
X, Y = map(int, input().split())

# Output result
print(can_build_closed_track(X, Y))