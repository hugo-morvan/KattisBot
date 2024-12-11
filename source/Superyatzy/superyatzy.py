import sys

# Read input values
N, M = map(int, input().split())
dice = list(map(int, input().split()))

# Check if it's possible to get Yatzy
if M >= N:
    print("Ja")
else:
    print("Nej")