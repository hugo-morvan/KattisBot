This is my solution to the problem: 
```python
n = int(input())
m = int(input())
balances = [int(input()) for _ in range(n)]
friends = [[int(input()) for j in range(2)] for i in range(m)]
# Calculate debts for each person
debt_dict = {}
for balance, person in zip(balances, range(n)):
    if balance > 0:
        debt_dict[person] = balance
    elif balance < 0:
        debt_dict[-balance] = -balance
# Calculate friendship pairs for each person
friendship_pairs = {}
for x,y in friends:
    if y not in friendship_pairs.keys():
        friendship_pairs[x] = [y]
    else:
        friendship_pairs[x].append(y)
# Check for debts to pay or receive
for person, debt in debt_dict.items():
    if len(friendship_pairs[person]) > 1:
        print("IMPOSSIBLE")
        exit()
    elif len(friendship_pairs[person]) == 0:
        print("POSSIBLE")
        exit()
# Check for debts to pay or receive
for person, debt in debt_dict.items():
    if len(friendship_pairs[person]) > 1:
        print("IMPOSSIBLE")
        exit()
    elif len(friendship_pairs[person]) == 0:
        print("POSSIBLE")
        exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0:
                print("IMPOSSIBLE")
                exit()
# Check for debt between friends
for person in friendship_pairs.keys():
    if len(debt_dict[person]) > 0:
        for friend in friendship_pairs[person]:
            if len(debt_dict[friend]) > 0
# Generator time: 45.2377 seconds