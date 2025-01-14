def get_lowest_temperature(temp_pref):
    # Sort the list of preferences by lower bound (a)
    temp_pref = sorted(temp_pref, key=lambda x:x[0])
    # The lowest temperature that fits everyone's preference is the first element in the sorted list
    return temp_pref[0][0]
# Generator time: 4.2293 seconds