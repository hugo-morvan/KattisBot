def determine_force_user(name, a, b, result):
    if name == "Obi-Wan Kenobi":
        if result == a - b:
            return "JEDI"
        elif result == abs(a - b):
            return "SITH"
        else:
            return "VEIT EKKI"
    elif name == "Anakin Skywalker":
        if result == a - b:
            return "SITH"
        elif result == abs(a - b):
            return "JEDI"
        else:
            return "VEIT EKKI"
    elif name == "Grogu":
        if result == a - b:
            return "VEIT EKKI"
        elif result == abs(a - b):
            return "VEIT EKKI"
        else:
            return "VEIT EKKI"

name = input()
a = int(input())
b = int(input())
result = int(input())

force_user_type = determine_force_user(name, a, b, result)
print(force_user_type)