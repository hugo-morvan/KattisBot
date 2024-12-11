# Read the number of transactions
N = int(input())

# Initialize the total expenses
total_expenses = 0

# Read each transaction and add it to the total expenses if it's negative
for _ in range(N):
    transaction = int(input())
    if transaction < 0:
        total_expenses += transaction

# Print the total expenses
print(total_expenses)