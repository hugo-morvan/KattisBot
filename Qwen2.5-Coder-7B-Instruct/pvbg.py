N = int(input())
R = list(map(int, input().split()))

# Initialize the number of waves
t = 1

# Iterate until all rows are protected
while True:
    # Check if the current wave can be defended
    if all(r >= t for r in R):
        break
    
    # Increment the wave number
    t += 1

print(t)
# Generator time: 4.6092 seconds