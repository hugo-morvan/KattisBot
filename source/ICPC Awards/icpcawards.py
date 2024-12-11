# Read input
N = int(input())
teams = []
for _ in range(N):
    university, team = input().split()
    teams.append((university, team))

# Sort teams by university and team name
teams.sort()

# Initialize lists for prizes
first_prizes = []
second_prizes = []
third_prizes = []

# Award prizes
for i, (university, team) in enumerate(teams):
    if i < 4:
        first_prizes.append((university, team))
    elif i < 8:
        second_prizes.append((university, team))
    else:
        third_prizes.append((university, team))

# Print the winners
print("\n".join(f"{university} {team}" for university, team in first_prizes))
print("\n".join(f"{university} {team}" for university, team in second_prizes))
print("\n".join(f"{university} {team}" for university, team in third_prizes))