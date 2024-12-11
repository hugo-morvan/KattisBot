def peano_addition(a, b):
    if a == "0":
        return b
    else:
        return "S(" + peano_addition(a[:-1], b) + ")"

def peano_multiplication(a, b):
    if a == "0" or b == "0":
        return "0"
    else:
        return peano_addition(peano_multiplication(a[:-1], b), a)

# Read input
x = input()
y = input()

# Compute the product
result = peano_multiplication(x, y)

# Output the result
print(result)