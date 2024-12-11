# Read input
N = int(input())
t_A, d_A = map(int, input().split())
t_B, d_B = map(int, input().split())

# Calculate total time for Alice
alice_time = sum(t_A + i * d_A for i in range(N))

# Calculate total time for Bob
bob_time = sum(t_B + i * d_B for i in range(N))

# Compare times and print result
if alice_time < bob_time:
    print("Alice")
elif alice_time > bob_time:
    print("Bob")
else:
    print("=")