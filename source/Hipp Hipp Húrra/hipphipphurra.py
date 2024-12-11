name = input()
age = int(input())

if age == 20:
    for _ in range(age):
        print("Hipp hipp hurra, " + name + "!")
elif age <= 20:
    for _ in range(age):
        print("Hipp hipp hurra, " + name + "!")
else:
    for _ in range(20):
        print("Hipp hipp hurra, " + name + "!")