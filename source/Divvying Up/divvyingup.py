# Read the number of contests
n = int(input())

# Read the prize purses for each contest
prize_purses = list(map(int, input().split()))

# Calculate the total prize money
total_prize_money = sum(prize_purses)

# Check if the total prize money can be evenly divided among three contestants
if total_prize_money % 3 == 0:
    print("yes")
else:
    print("no")