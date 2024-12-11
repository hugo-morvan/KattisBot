def wind_level(wind_speed):
    if 0 <= wind_speed < 0.2:
        return "Logn"
    elif 0.3 <= wind_speed < 1.5:
        return "Andvari"
    elif 1.6 <= wind_speed < 3.3:
        return "Kul"
    elif 3.4 <= wind_speed < 5.4:
        return "Gola"
    elif 5.5 <= wind_speed < 7.9:
        return "Stinningsgola"
    elif 8.0 <= wind_speed < 10.7:
        return "Kaldi"
    elif 10.8 <= wind_speed < 13.8:
        return "Stinningskaldi"
    elif 13.9 <= wind_speed < 17.1:
        return "Allhvass vindur"
    elif 17.2 <= wind_speed < 20.7:
        return "Hvassvidri"
    elif 20.8 <= wind_speed < 24.4:
        return "Stormur"
    elif 24.5 <= wind_speed < 28.4:
        return "Rok"
    elif 28.5 <= wind_speed < 32.6:
        return "Ofsavedur"
    else:
        return "Farvidri"

# Read input
wind_speed = float(input())

# Get wind level
level = wind_level(wind_speed)

# Print output
print(level)