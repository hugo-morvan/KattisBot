# Read input values
N, M = map(int, input().split())

# Calculate the remainder of chicken pieces
remainder = M % N

# Determine the outcome based on the remainder
if remainder == 0:
    print(f"Dr. Chaz will have {M} pieces of chicken left over!")
else:
    needed = N - remainder
    print(f"Dr. Chaz needs {needed} more pieces of chicken!")