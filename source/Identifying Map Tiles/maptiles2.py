def quadkey_to_coordinates(quadkey):
    zoom = len(quadkey)
    x = 0
    y = 0
    
    for i in range(zoom - 1, -1, -1):
        bit = int(quadkey[i])
        if bit == 0:
            pass
        elif bit == 1:
            x += 2 ** (zoom - 1 - i)
        elif bit == 2:
            y += 2 ** (zoom - 1 - i)
        else:
            x += 2 ** (zoom - 1 - i)
            y += 2 ** (zoom - 1 - i)
    
    return zoom, x, y

# Read input
quadkey = input()

# Get coordinates
zoom, x, y = quadkey_to_coordinates(quadkey)

# Print output
print(zoom, x, y)