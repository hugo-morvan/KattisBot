def detect_zombie(message):
    smileys = message.count(':)')
    frowns = message.count(':(')
    
    if smileys > 0 and frowns == 0:
        return "alive"
    elif frowns > 0 and smileys == 0:
        return "undead"
    elif smileys > 0 and frowns > 0:
        return "double agent"
    else:
        return "machine"

# Read input
input_message = input()

# Detect and print the result
output = detect_zombie(input_message)
print(output)