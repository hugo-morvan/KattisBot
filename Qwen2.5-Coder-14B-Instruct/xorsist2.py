def xor_from_1_to_n(n):
    if n % 8 == 0:
        return n
    elif n % 8 == 1:
        return 1
    elif n % 8 == 2:
        return n + 1
    elif n % 8 == 3:
        return 0
    elif n % 8 == 4:
        return n
    elif n % 8 == 5:
        return n + 1
    elif n % 8 == 6:
        return 0
    else:  # n % 8 == 7
        return 1

def xor_from_a_to_b(a, b):
    return xor_from_1_to_n(b) ^ xor_from_1_to_n(a - 1)

N = int(input())
a, b = map(int, input().split())

result = xor_from_a_to_b(a, b)
if result == 0:
    print("Enginn")
elif result <= N:
    print(result)
else:
    print("Gunnar")
# Generator time: 31.7577 seconds