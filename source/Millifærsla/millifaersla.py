# Read the transaction fees from the input
a = int(input())
b = int(input())
c = int(input())

# Determine the service with the lowest transaction fee
if a < b and a < c:
    print("Monnei")
elif b < a and b < c:
    print("Fjee")
else:
    print("Dolladollabilljoll")